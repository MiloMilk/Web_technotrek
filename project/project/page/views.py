from django.shortcuts import render, HttpResponse

# Create your views here.
def Page(response, num):
    return HttpResponse("Page")
