#!/usr/bin/env python
# coding:utf-8

from app01 import models
from django.shortcuts import HttpResponse


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


def test(request):
    x = handle_local_path(3, 2, 28)
    print(x)
    return HttpResponse('ok')


def check_select(request):
    info_dic = {}
    success_list = []
    error_list = []
    push_target_id = request.POST['PushTarget']
    production_line_id = request.POST['productions-line']
    production_id = request.POST['production']
    if int(push_target_id) == 1:
        error_list.append('未选择发布环境')
    else:
        success_list.append('已选择发布环境')
    if not production_line_id.isdigit():
        error_list.append('未选择产品线')
    else:
        success_list.append('已选择产品线')
    if not production_id.isdigit():
        error_list.append('未选择产品')
    else:
        success_list.append('已选择产品')
    info_dic['error'] = error_list
    info_dic['success'] = success_list
    info_dic['pt_id'] = push_target_id
    info_dic['pl_id'] = production_line_id
    info_dic['p_id'] = production_id
    return info_dic


def handle_local_path(pushtarget_id, prod_line_id, prod_id):
    push_name = models.PushTarget.objects.get(id=pushtarget_id).target_name
    prod_line_name = models.ProductionLine.objects.get(id=prod_line_id).pl_name
    prod_name = models.Production.objects.get(id=prod_id).p_name
    dir_path = 'upload/%s/%s' % (push_name, prod_line_name)
    import os
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/%s.war' % (dir_path, prod_name)
    return file_path

