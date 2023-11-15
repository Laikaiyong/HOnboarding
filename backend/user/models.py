from django.db import models

import uuid

from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=60, unique=True, blank=True, null=True)

    USER_ROLE = (
        ("Super Admin", "Super Admin"),
        ("Staff", "Staff"),
    )
    role = models.CharField(choices=USER_ROLE, max_length=200, blank=True, null=True)

    objects: UserManager = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "role", "username"]

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
