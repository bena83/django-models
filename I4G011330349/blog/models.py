from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class Post(models.Model):
  Title= models.CharField(max_length=200)
  Text= models.TextField(max_length=255)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  Created_date = models.DateField()
  Published_date= models.CharField(max_length=100)
