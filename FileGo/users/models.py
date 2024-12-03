from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ExpandedUser(User):
    class Meta:
        proxy = True

    def get_profile_picture(self):
        pass
