"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from django.urls import path, re_path
from home.views import home
from account.views import account
from post.views import post, EditPost
from categories.views import category, categoryedit
from addpost.views import addpost
from addcategory.views import addcategory
from core.views import Login

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^core/login/$', Login.as_view(), name= "login"),
    re_path(r'^$', home, name='home'),
    re_path(r'^account/(?P<name>\w+)/$', login_required(account), name = "account"),
    re_path(r'^category/(?P<ck>\d+)/$', category, name='category'),
    re_path(r'^category/(?P<ck>\d+)/edit$', login_required(categoryedit), name='categoryedit'),
    re_path(r'^post/(?P<pk>\d+)/$', post, name='post'),
    re_path(r'^post/(?P<pk>\d+)/edit$', EditPost.as_view(), name='editpost'),
    re_path(r'^addpost/$', login_required(addpost), name='addpost'),
    re_path(r'^addcategory/$', login_required(addcategory), name='addcategory'),

    re_path(r'^accounts/profile/$', account)
]
