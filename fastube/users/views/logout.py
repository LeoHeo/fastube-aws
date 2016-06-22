from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib import messages
from django.conf import settings


class LogoutView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        messages.add_message(
            self.request,
            messages.SUCCESS,
            settings.LOGOUT_SUCCESS_MESSAGE,
        )
        return reverse("home")
