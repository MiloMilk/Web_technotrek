from django.shortcuts import render, HttpResponse
from post.models import Post
# Create your views here.
def account(response, name=None):

#    context = {
#        "posts": Post.objects.get(author=response.user)
#    }

    if None:
        return render(response, 'account/account.html', {})
    else:
        return HttpResponse("Author " + str(response.user) + " has not posts")