from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models


class User(AbstractUser):

    phonenumber = models.CharField(
        max_length=6,
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse("home")
