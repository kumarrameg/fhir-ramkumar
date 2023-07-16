import os
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
  AbstractBaseUser,
  PermissionsMixin,
  BaseUserManager,
)

class UserManager(BaseUserManager):
  """
    Custom manager for the User model.
  """

  def create_user(self, email, password=None, **extra_fields):
    """
        Creates and saves a new user with the given email and password.
        Raises a ValueError if the email is not provided.
    """

    if not email:
      raise ValueError('The Email must be set')
    user = self.model(email=self.normalize_email(email),**extra_fields)
    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_superuser(self,email,password):
    """
        Creates and saves a new superuser with the given email and password.
        Sets is_staff and is_superuser to True.
    """

    user =self.create_user(email,password)
    user.is_staff= True
    user.is_superuser = True
    user.save(using=self._db)

    return user


class User(AbstractBaseUser,PermissionsMixin):
  """
    Represents a user in the system.
  """
  email = models.EmailField(max_length=255,unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects =  UserManager()

  USERNAME_FIELD = 'email'



