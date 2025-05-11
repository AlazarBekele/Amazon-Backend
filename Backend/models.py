from django.db import models

# Create your models here.

class Login_IMG (models.Model):

  title = models.CharField (max_length=20)
  picture = models.ImageField (upload_to='photo/')

  def __str__(self):
    return self.title
  


class Shopping_Object (models.Model):

  Obj_name = models.CharField (max_length=200)
  Obj_Image = models.ImageField (upload_to='shop/', null=True, blank=True)
  Obj_rate = models.IntegerField ()
  Obj_quantity = models.IntegerField ()
  Obj_price = models.IntegerField ()

  def __str__(self):
    return self.Obj_name