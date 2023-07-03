from django import forms
from django.core.exceptions import ValidationError
from web import models
from utils.bootstrap import BootStrapForm


class OrderModalForm(BootStrapForm, forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ["url", "count"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        price_count_list = []
        text_count_list = []
        queryset = models.PricePolicy.objects.all().order_by('count')

        for item in queryset:
            unit_price = item.price / item.count
            price_count_list.append([item.count, ">={} ￥{}/条".format(item.count, unit_price), unit_price])
            text_count_list.append(">={} ￥{}/条".format(item.count, unit_price))

        if text_count_list:
            self.fields['count'].help_text = "，".join(text_count_list)
        else:
            self.fields['count'].help_text = "请联系管理员设置价格"

        self.price_count_list = price_count_list

    def clean_count(self):
        count = self.cleaned_data['count']
        if not self.price_count_list:
            raise ValidationError("请联系管理员设置价格")
        min_count_limit = self.price_count_list[0][0]

        if count < min_count_limit:
            raise ValidationError("最低支持数量为{}".format(min_count_limit))
        return count
