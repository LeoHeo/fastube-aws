from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


class LogoutView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return reverse("home")
