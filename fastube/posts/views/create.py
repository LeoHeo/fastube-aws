from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from posts.models import Post


class PostCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "posts/new.html",
            context={
                "header": "New Post",
                "action": reverse("posts:confirm"),
            },
        )

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        content = request.POST.get("content")
        video_id = request.POST.get("video_id")

        post = Post.objects.create(
            user=request.user,
            video_id=video_id,
            title=title,
            content=content,
        )

        return redirect("posts:list")


class PostCreateConfirmView(View):

    def get(self, request, *args, **kwargs):
        return redirect("posts:create")

    def post(self, request, *args, **kwargs):
        video_id = request.POST.get("video_id")
        title = request.POST.get("title")
        content = request.POST.get("content")

        return render(
            request,
            "posts/new.html",
            context={
                "header": "Confirm Post",
                "action": reverse("posts:create"),
                "video_id": video_id,
                "title": title,
                "content": content,
            }
        )
