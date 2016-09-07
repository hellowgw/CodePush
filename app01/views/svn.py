#!/usr/bin/env python
# coding:utf-8
from django.shortcuts import render


def get_svn(request):
    return render(request, 'main/svn.html')
