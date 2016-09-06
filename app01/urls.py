"""CodePush URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from app01.views import layout, login

urlpatterns = [
    url(r'^login/$', layout.run_rollback),
    url(r'^svn/$', layout.get_svn),
    url(r'^package/$', layout.upload_package),
    url(r'^rollback/$', layout.run_rollback),
    url(r'^data/$', layout.data),
    url(r'^get_pro_info/$', layout.get_production_info),
    url(r'^$', login.login),
]
