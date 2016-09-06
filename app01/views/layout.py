#!/usr/bin/env python
# coding:utf-8

from django.shortcuts import render
from django.shortcuts import HttpResponse
from app01 import models
from app01.forms.main_form import PackageForm
from django.views.decorators.csrf import csrf_exempt


def get_production_info(request):
    id_type = request.GET.keys()[0]
    submit_id = request.GET[id_type]
    data_dic = {}
    if id_type == 'target_id':
        data_obj = models.ProductionLine.objects.filter(target_id=int(submit_id))
        for pl in data_obj:
            data_dic[pl.id] = pl.pl_cname
    else:
        data_obj = models.Production.objects.filter(production_line_id=int(submit_id))
        for p in data_obj:
            data_dic[p.id] = p.p_cname
    import json
    return HttpResponse(json.dumps(data_dic))





@csrf_exempt
def data(request):
    upload_obj = PackageForm()
    if request.method == 'POST':
        ajax_data = request.POST
        print(type(ajax_data))
        upload_obj = PackageForm(**ajax_data)
        return render(request, 'main/package.html', {'upload': upload_obj})

    return render(request, 'main/package.html', {'upload': upload_obj})


def get_svn(request):
    return render(request, 'main/svn.html')


@csrf_exempt
def upload_package(request):
    upload_obj = PackageForm()
    if request.method == 'POST':
        upload_info_obj = request.POST
        if upload_info_obj.is_valid():
            upload_info = upload_info_obj.clean()
            print(upload_info)

    return render(request, 'main/package.html', {'upload': upload_obj})


def run_rollback(request):
    return render(request, 'main/rollback.html')