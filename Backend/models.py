from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Login_IMG (models.Model):

  title = models.CharField (max_length=20)
  picture = models.ImageField (upload_to='photo/')

  def __str__(self):
    return self.title
  
class Category (models.Model):

  Type = models.CharField (max_length=30)

  def __str__(self):
    return self.Type

class Shopping_Object (models.Model):

  Obj_name = models.CharField (max_length=200)
  Obj_Image = models.ImageField (upload_to='shop/', null=True, blank=True)
  Obj_rate = models.IntegerField ()
  Obj_quantity = models.IntegerField ()
  Obj_price = models.IntegerField ()
  Obj_Category = models.ForeignKey (Category, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    return self.Obj_name
  

class Profile_picture (models.Model):

  user = models.OneToOneField (User, on_delete=models.CASCADE)
  Profile_IMG = models.ImageField (upload_to='Profile/', default='default.jpg')
  Category_Type = models.ForeignKey (Category, on_delete=models.SET_NULL, blank=True, null=True)

  def __str__(self):
    return self.user.username
  

class Sell_object_container (models.Model):

  Sell_Object_name = models.CharField (max_length=200)
  Sell_object_Discription = models.TextField (null=True, blank=True)
  Sell_Object_Image = models.ImageField (upload_to='Sell_Object/', null=True, blank=True)
  Sell_Object_quantity = models.IntegerField ()
  Sell_Object_price = models.IntegerField ()
  Sell_Object_Category = models.ForeignKey (Category, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    return self.Sell_Object_name