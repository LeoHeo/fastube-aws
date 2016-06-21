from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings


class SignupView(TemplateView):
    template_name = "users/signup.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        phonenumber = request.POST.get("phonenumber")

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            email=email,
            phonenumber=phonenumber,
        )

        messages.add_message(
            request,
            messages.SUCCESS,
            settings.SIGNUP_SUCCESS_MESSAGE,
        )

        return redirect(user)
