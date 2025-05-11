from django.contrib import admin
from .models import (

  Category,
  Login_IMG,
  Shopping_Object

)

# Register your models here.

admin.site.register (Login_IMG)
admin.site.register (Shopping_Object)
admin.site.register (Category)