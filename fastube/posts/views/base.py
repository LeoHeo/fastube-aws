from django.views.generic.base import View

from posts.models import Post


class PostBaseView(View):
    model = Post
