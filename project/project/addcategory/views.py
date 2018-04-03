from django.shortcuts import render, redirect, HttpResponse
from django import forms
from categories.models import Category
# Create your views here.

class AddCategoryForm(forms.Form):
    name = forms.CharField(required=True)

def addcategory(request):
    if request.method == 'GET':
        form = AddCategoryForm()
        return render(request, 'addcategory/addcategory style.html', {'form':form})
    elif request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            category = Category(name=data['name'])
            category.author = request.user
            category.save()
            return redirect('/')
        else:
            return render(request, 'addcategory/addcategory style.html', {'form': form})


    return HttpResponse("Thank YOU")