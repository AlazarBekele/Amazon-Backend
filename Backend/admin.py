from django.contrib import admin
from .models import (

  Category,
  Login_IMG,
  Shopping_Object,
  Profile_picture,
  Sell_object_container
)

# Register your models here.

admin.site.register (Login_IMG)
admin.site.register (Shopping_Object)
admin.site.register (Category)
admin.site.register (Profile_picture)
admin.site.register (Sell_object_container)