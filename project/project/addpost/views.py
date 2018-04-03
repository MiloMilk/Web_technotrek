from django.shortcuts import render, HttpResponse
from django import forms
from django.views.generic import UpdateView
from post.models import Post
# Create your views here.

class AddPostForm(forms.Form):
    header = forms.CharField(required=True)

class AddPost(UpdateView):
    model = Post
    fields = 'name', 'author', 'bodytext'
    template_name = 'addpost/addpost style.html'

def addpost(request):
    if request.method == 'GET':
        form = AddPostForm()
        return render(request, 'addpost/addpost style.html', {'form':form})
    elif request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            pass
        else:
            return render(request, 'addpost/addpost style.html', {'form': form})


    return HttpResponse("Thank YOU")