from django.urls import re_path
from core.views import Login, Logout

app_name = 'core'

urlpatterns = [
    re_path(r'^login/$', Login.as_view(), name="login"),
    re_path(r'^logout/$', Logout.as_view(), name="logout"),
]