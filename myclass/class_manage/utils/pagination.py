# """
# 自定义分页组件
# 在属兔函数中
# def student_list(request):
#     # 1. 根据情况去筛查自己的数据
#     queryset = models.UserInfo.objects.all()
#
#     # 2. 实例化分页对象
#     page_object = Pagination(request, queryset)
#
#     context = {'queryset': page_object.page_queryset,  分完页的数据
#         "page_string": page_object.html()    生成页码
#         }
#
#     return render(request, 'student_list.html', context)
# 在HTML页面中
# {% for obj in queryset %}
#
# {% endfor%}
#
# <ul class="pagination">
#       {{ page_string }}
# </ul>
# """
from django.utils.safestring import mark_safe


class Pagination(object):

    def __init__(self, request, queryset, page_param="page", page_size=4, plus=2):
        """
        :param request: 请求的对象
        :param queryset: 符合条件的数据（根据这个数据进行分页处理）
        :param page_param:每页显示多少条数据
        :param page_size:在URL中传递到获取分页参数，例如：/list/?page=12
        :param plus:显示当前页的前几页，后几页
        """

        from django.http.request import QueryDict
        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        page = request.GET.get(page_param, "1")

        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset = queryset[self.start:self.end]

        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = self.page * 2 + 1
            else:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        page_str_list = []

        # 首页
        self.query_dict.setlist(self.page_param, [1])

        page_str_list.append('<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
            page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            self.query_dict.urlencode()
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
            page_str_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))

        search_string = """
            <li>
                <form method="get" style="float: left;margin-left: -1px">
                    <div class="input-group" style="width: 200px">
                        <input name="page"
                            style="position: relative;float: left;display: inline-block;width: 80px;border-radius: 0"
                            type="text" class="form-control" placeholder="页码">
                        <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
                    </div>
                </form>
            </li>"""

        page_str_list.append(search_string)

        page_string = mark_safe("".join(page_str_list))

        return page_string
