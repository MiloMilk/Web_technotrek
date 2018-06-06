from django.urls import re_path
from account.views import account

app_name = 'account'

urlpatterns = [

    re_path(r'^profile/$', account, name="profile"),
    re_path(r'^(?P<name>\w+)/$', account, name="account"),
]
