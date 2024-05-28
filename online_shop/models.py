from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"ID: {self.pk} | Username: {self.username}"


class Categories(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return f"Category name: {self.name}"


class Products(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='documents/images', blank=True, null=True)
    audio = models.FileField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    doc = models.FileField(blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f"Category name: {self.category_id.name} | Product name: {self.name}"


class Orders(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"User ID: {self.user_id.name} | Product ID: {self.product_id.name} | TIME: {self.created}"