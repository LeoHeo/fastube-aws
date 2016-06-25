from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from posts.models import Post
from posts.utils import youtube


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
        thumbnail_image = request.FILES.get("thumbnail_image")

        post = Post.objects.create(
            user=request.user,
            video_id=video_id,
            title=title,
            content=content,
            thumbnail_image=thumbnail_image,
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
                "youtube_origin_url": youtube.get_youtube_original_url_by_video_id(video_id),
                "youtube_embed_url": youtube.get_youtube_embed_url_by_video_id(video_id),
                "youtube_thumbnail_image_url": youtube.get_youtube_thumbnail_image_url_by_video_id(video_id),
            }
        )
