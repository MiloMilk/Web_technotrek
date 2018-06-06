from django.shortcuts import render, HttpResponse, reverse
from .models import Post, Comment, Like
from django.views.generic import UpdateView, DetailView, View
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django import forms
from categories.models import Category

# Create your views here.
def post(response, pk = None):

    post = Post.objects.get(id=pk)


    comments = Comment.objects.filter(article_id=post.id)
    context = {
        "post": post,
        "comment": comments,
    }

    return render(response, "post/post style.html", context)


class EditPost(UpdateView):
    model = Post
    fields = 'name', 'bodytext', 'categories', 'image'
    context_object_name = 'post'
    template_name = 'post/editpost.html'

    def dispatch(self, request, pk=None, *args, **kwargs):
        if Post.objects.get(id=pk).author != request.user:
            return HttpResponse(u"ПШЕЛ ОТСЮДА")
        else:
            return super(EditPost, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("post:post", kwargs={'pk': self.object.pk})




class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = 'name', 'bodytext', 'categories', 'image'

def addpost(request):

    post = Post(author=request.user)
    if request.method == 'GET':
        form = AddPostForm(instance=post)
        return render(request, 'post/addpost style.html', {'form':form})
    elif request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save()

            return redirect('/')
        else:
            return render(request, 'post/addpost style.html', {'form': form})


    return HttpResponse("Thank YOU")


def postcommentview(request, pk = None):

    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(article_id=post.id).prefetch_related('commentLike')

    context = {
        "comment": comments,
    }

    return render(request, "post/comments.html", context)



class CommentLikeAjaxView(View):

    def dispatch(self, request, pk=None, *args, **kwargs):
        # Забираем из базы пост, который собираются лайкнуть
        self.comment_object = get_object_or_404(Comment, id=pk)
        return super(CommentLikeAjaxView, self).dispatch(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        if not Like.objects.filter(author=self.request.user, comment=self.comment_object).exists():
            like = Like(author=self.request.user, comment=self.comment_object)
            like.save()
        
        return HttpResponse()

def putcomment(request, pk = None):
    num = len(Comment.objects.all())
    print(num)
    print(request.POST)

    comment = Comment(article_id=Post.objects.get(id=pk), author=request.user)
    comment.content = request.POST.get('message')
    comment.save()

    return redirect('/post/'+str(pk)+'/')