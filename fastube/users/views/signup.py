from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from users.models import User


class SignupView(TemplateView):
    template_name = "users/signup.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        phonenumber = request.POST.get("phonenumber")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            phonenumber=phonenumber,
        )

        return redirect(user)
