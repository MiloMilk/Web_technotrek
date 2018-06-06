from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

class Login(LoginView):
    template_name = "core/login.html"


class Logout(LogoutView):
    next_page = '/'
    template_name = "core/logout.html"
