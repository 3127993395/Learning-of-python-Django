from django.urls import reverse


def filter_reverse(request, url):
    # 1.获取permission中的filter参数
    filter_string = request.GET.get("_filter")
    if not filter_string:
        return url
    # 2.URL进行拼接
    # return redirect(reverse("customer_list") + "?{}".format(filter_string))
    return reverse("customer_list") + "?{}".format(filter_string)