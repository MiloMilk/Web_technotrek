from django.contrib.auth.decorators import login_required
from django.urls import re_path
from post.views import post, EditPost, addpost, postcommentview, CommentLikeAjaxView, putcomment

from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

app_name = 'post'

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', post, name='post'),
    re_path(r'^(?P<pk>\d+)/edit$', login_required(EditPost.as_view()), name='editpost'),
    re_path(r'^addpost/$', login_required(addpost), name='addpost'),
    re_path(r'^(?P<pk>\d+)/comments$', postcommentview, name='comments'),
    re_path(r'^(?P<pk>\d+)/like', csrf_exempt(login_required(CommentLikeAjaxView.as_view())), name='likeadd'),
    re_path(r'^(?P<pk>\d+)/putcomment', login_required(putcomment), name='putcomment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
