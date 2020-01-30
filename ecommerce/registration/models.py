from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)


class UserManager(BaseUserManager):

    def create_user(self, email, username, password, phone_number):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    customer_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15)
    #avatar = models.ImageField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
