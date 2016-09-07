#!/usr/bin/env python
# coding:utf-8
from django.shortcuts import render
from app01.forms.main_form import PackageForm


def upload_package(request):
    upload_obj = PackageForm()
    if request.method == 'POST':
        push_target_id = request.POST['PushTarget']
        production_line_id = request.POST['productions-line']
        production_id = request.POST['production']
        upload_file_obj = request.FILES.get('upload_file')
        success_msg_list = []
        err_msg_list = []
        if int(push_target_id) == 1:
            err_msg_list.append('没有选择发布环境')
        if not production_line_id.isdigit():
            err_msg_list.append('没有选择产品线')
        if not production_id.isdigit():
            err_msg_list.append('没有选择产品')
        if not upload_file_obj:
            err_msg_list.append('没有指定上传数据')
        if err_msg_list:
            return render(request, 'main/package.html', {'upload': upload_obj, 'err_msg': err_msg_list})
        else:
            success_msg_list.append('上传条件满足')
            file_name = upload_file_obj.name
            upload_path = 'upload/%s' % file_name
            with open(upload_path, 'wb') as f:
                for data in upload_file_obj.chunks():
                    f.write(data)
            return render(request, 'main/package.html', {'upload': upload_obj, 'success_msg': success_msg_list})

    return render(request, 'main/package.html', {'upload': upload_obj})
