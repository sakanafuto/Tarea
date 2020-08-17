from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model

class User(models.Model):
  username = models.CharField(max_length=50)

  def __str__(self): 
    return self.username

class Task(models.Model):
  title = models.CharField(max_length=20)
  pub_date = models.DateTimeField(default=timezone.now)
  caption = models.TextField(max_length=255)
  completed = models.BooleanField(default=False)
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  

  def __str__(self): 
    return self.title