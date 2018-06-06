from django.shortcuts import render, HttpResponse
from post.models import Post
from core.models import User
# Create your views here.
def account(response, name=None):

    try:
        context = {
            "posts": Post.objects.filter(author = response.user)
        }
        if context["posts"]:
            return render(response, 'account/account.html', context)
        else:
            return HttpResponse("Author " + str(response.user) + " has not posts")
    except:
        return HttpResponse("Login first")