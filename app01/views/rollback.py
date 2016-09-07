#!/usr/bin/env python
# coding:utf-8
from django.shortcuts import render


def run_rollback(request):
    return render(request, 'main/rollback.html')
