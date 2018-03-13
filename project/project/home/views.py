from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(response):
    return HttpResponse("HomePage")