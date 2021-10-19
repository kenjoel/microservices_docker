from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    likes = models.PositiveIntegerField()


class User(models.Model):
    pass


