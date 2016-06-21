from django.contrib import messages
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


class LogoutView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "성공적으로 로그아웃 되었습니다.",
        )
        return reverse("home")
