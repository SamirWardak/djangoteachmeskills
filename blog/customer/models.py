from django.db import models
from django.contrib.auth.models import AbstractUser


USER_TYPE = [
    ('admin', 'Админ'),
    ('user', 'Юзер'),
    ('editor', 'Едитор'),
]

class Profile(AbstractUser):
    type = models.CharField(max_length=255, choices=USER_TYPE, default='user')
    pass

# Create your models here.
