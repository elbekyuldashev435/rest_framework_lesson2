from django.contrib import admin
from .models import Users, Categories, Products, Orders
# Register your models here.


admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Orders)