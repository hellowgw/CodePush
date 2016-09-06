#!/usr/bin/env python
# coding:utf-8

from django import forms
from app01 import models


class PackageForm(forms.Form):

    PushTarget = forms.ChoiceField(widget=forms.Select(), choices=(),)

    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)
        self.fields['PushTarget'].widget.choices = models.PushTarget.objects.all().values_list('id', 'target_cname')