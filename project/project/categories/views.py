from django.shortcuts import render, HttpResponse, redirect
from .models import Category
from django import forms
# Create your views here.

class AddCategoryForm(forms.ModelForm):
    #name = forms.CharField(required=True)
    class Meta:
        model = Category
        fields = 'name',

# Create your views here.
def category(request, ck = None):

    context = {
        'category': Category.objects.get(id=ck)
    }

    return render(request, 'categories/category.html', context)

def categoryedit(request, ck = None):

    category = Category.objects.get(id=ck)
    if category.author != request.user:
        return HttpResponse(u"ПОШЕЛ НА***")

    if request.method == 'GET':
        form = AddCategoryForm(instance=category)
        return render(request, 'categories/categoryedit.html', {'form':form, 'category':category})
    elif request.method == 'POST':
        form = AddCategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('/category/'+str(category.id)+'/')
        else:
            return render(request, 'categories/categoryedit.html', {'form': form, 'category':category})

