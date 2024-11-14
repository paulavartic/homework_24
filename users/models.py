from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Email", help_text="Your email", unique=True)
    phone = models.CharField(
        verbose_name="Phone number",
        help_text="Your phone number",
        max_length=35,
        blank=True,
        null=True,
    )
    town = models.CharField(
        verbose_name="Town",
        help_text="Where are you from?",
        max_length=40,
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        verbose_name="Photo",
        help_text="Your photo",
        upload_to="users/avatars",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.id
