from django import forms

from web import models
from utils.bootstrap import BootStrapForm


class PolicyModelForm(BootStrapForm, forms.ModelForm):
    class Meta:
        model = models.PricePolicy
        fields = ['count', 'price']
