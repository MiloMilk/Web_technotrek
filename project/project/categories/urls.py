from django.contrib.auth.decorators import login_required
from django.urls import re_path
from categories.views import category, categoryedit, addcategory

app_name = 'categories'

urlpatterns = [

    re_path(r'^(?P<ck>\d+)/$', category, name='category'),
    re_path(r'^(?P<ck>\d+)/edit$', login_required(categoryedit), name='categoryedit'),
    re_path(r'^addcategory/$', login_required(addcategory), name='addcategory'),
]
