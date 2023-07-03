from django.template.library import Library
from web import models

register = Library()


@register.filter
def color(num):
    return models.TransactionRecord.charge_type_class_mapping[num]
