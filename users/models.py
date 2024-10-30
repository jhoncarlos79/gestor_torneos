from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True) # Añadimos para loguearse con el email
    # Comentar las lineas para poder crear superusuarios
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]