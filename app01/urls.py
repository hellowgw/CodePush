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
from app01.views import comm
from app01.views import login
from app01.views import svn
from app01.views import package
from app01.views import rollback

urlpatterns = [
    url(r'^login/$', login.login),
    url(r'^test/$', comm.test),
    url(r'^svn/$', svn.get_svn),
    url(r'^package/$', package.upload_package),
    url(r'^rollback/$', rollback.run_rollback),
    url(r'^get_pro_info/$', comm.get_production_info),
    url(r'^$', login.login),
]
