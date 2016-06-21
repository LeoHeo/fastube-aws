from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


class LoginView(TemplateView):
    template_name = "users/login.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next") or "home"

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            return redirect(next_url)

        return redirct("auth:login")
