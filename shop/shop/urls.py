"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='shop2/shop2.html'), name='shop2'),
    path('userlist', views.userlist, name='userlist'),
    path('useradd', views.useradd, name='useradd'),
    path('useraddimpl', views.useraddimpl, name='useraddimpl'),
    path('userdetail', views.userdetail, name='userdetail'),

    path('userupdate', views.userupdate, name='userupdate'),
    path('userupdateimpl', views.userupdateimpl, name='userupdateimpl'),
    path('userdelete', views.userdelete, name='userdelete'),

    path('itemlist', views.ItemView.itemlist, name='itemlist'),
    path('itemdetail', views.ItemView.itemdetail, name='itemdetail'),
    path('itemadd', views.ItemView.itemadd, name='itemadd'),
    path('itemaddimpl', views.ItemView.itemaddimpl, name='itemaddimpl'),
    path('itemupdate', views.ItemView.itemupdate, name='itemupdate'),
    path('itemupdateimpl', views.ItemView.itemupdateimpl, name='itemupdateimpl'),

    path('login', views.MainView.login, name='login'),
    path('loginimpl', views.MainView.loginimpl, name='loginimpl'),
    path('logout', views.MainView.logout, name='logout'),
]
