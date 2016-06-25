from django.views.generic.list import ListView

from .base import PostBaseView
from posts.models import Post


class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_list = "post_list"
