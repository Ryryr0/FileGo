from django.db import models
from django.contrib.auth.models import User


class MyUser(User):
    class Meta:
        proxy = True

    def get_profile_picture(self):
        pass
