from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from fastube.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^', include('users.urls.auth', namespace="users")),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^posts/', include('posts.urls.posts', namespace="posts")),
    url(r'^api/', include('posts.urls.list', namespace="api")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
