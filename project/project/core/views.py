from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView
# Create your views here.

class Login(LoginView):

    template_name = "core/login.html"