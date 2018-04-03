from django.shortcuts import render, HttpResponse
from categories.models import Category
from post.models import Post

# Create your views here.
def home(request):

    sort = request.GET.get('sort')
    if sort == None:
        sort = 'id'

    posts = Post.objects.all().order_by(sort)

    length = len(posts)
    length = length + 1

    search = request.GET.get('search')
    if search != None:
        posts = posts.filter(name__contains=search)


    context = {
        'categories': Category.objects.all(),
        'news': posts,
        'length': length
    }

    return render(request, 'home/home_page.html', context)