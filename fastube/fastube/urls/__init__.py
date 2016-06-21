from django.conf.urls import url, include
from django.contrib import admin

from fastube.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^', include('users.urls.auth', namespace="users")),
    url(r'^$', HomeView.as_view(), name="home"),
]
