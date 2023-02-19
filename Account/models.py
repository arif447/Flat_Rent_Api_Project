from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,\
    PermissionsMixin
from django.conf import settings

# Create your models here.


class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Must use email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User_create(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=100,)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.user_name


class User_Profile(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100,)
    lastname = models.CharField(max_length=100,)
    address = models.CharField(max_length=200,)

    def __str__(self):
        return self.firstname + self.lastname
