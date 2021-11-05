from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)



