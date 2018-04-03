from django.shortcuts import render, HttpResponse, reverse
from .models import Post
from django.views.generic import UpdateView

# Create your views here.
def post(response, pk = None):

    context = {
        "post": Post.objects.get(id = pk)
    }

    return render(response, "post/post style.html", context)


class EditPost(UpdateView):
    model = Post
    fields = 'name', 'bodytext'
    context_object_name = 'post'
    template_name = 'post/editpost.html'

    def get_success_url(self):
        return reverse("post", kwargs={'pk': self.object.pk})