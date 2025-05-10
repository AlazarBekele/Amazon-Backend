from django.db import models

# Create your models here.

class Login_IMG (models.Model):

  title = models.CharField (max_length=20)
  picture = models.ImageField (upload_to='photo/')

  def __str__(self):
    return self.title