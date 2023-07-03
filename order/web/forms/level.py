from web import models
from django import forms
from utils.bootstrap import BootStrapForm


class LevelModelForm(BootStrapForm, forms.ModelForm):
    class Meta:
        model = models.Level
        fields = ['title', 'percent']