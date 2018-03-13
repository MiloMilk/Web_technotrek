from django.shortcuts import render, HttpResponse

# Create your views here.
def Account(response):
    name = response.GET.get('name')
    return HttpResponse("{}s account page".format(name))

