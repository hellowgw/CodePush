#!/usr/bin/env python
# coding:utf-8
from django.shortcuts import render
from app01.forms.main_form import PackageForm
from app01.views.comm import handle_local_path
from app01.views.comm import check_select


def upload_package(request):
    upload_obj = PackageForm()
    if request.method == 'POST':
        msg_dic = check_select(request)
        success_msg_list = msg_dic['success']
        err_msg_list = msg_dic['error']
        upload_file_obj = request.FILES.get('upload_file')

        if not upload_file_obj:
            err_msg_list.append('未来指定数据包')
        else:
            success_msg_list.append('已指定数据包')
        if err_msg_list:
            return render(request, 'main/package.html', {'upload': upload_obj, 'err_msg': err_msg_list})
        else:
            # upload_file_size = upload_file_obj.size
            upload_path = handle_local_path(int(msg_dic['pt_id']), int(msg_dic['pl_id']), int(msg_dic['p_id']))
            with open(upload_path, 'wb') as f:
                for data in upload_file_obj.chunks():
                    f.write(data)
            success_msg_list.append('上传代码包成功')
            return render(request, 'main/package.html', {'upload': upload_obj, 'success_msg': success_msg_list})

    return render(request, 'main/package.html', {'upload': upload_obj})
