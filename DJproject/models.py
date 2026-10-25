from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)


# Работники магазина
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=40)  # Должность
    phone = models.CharField(max_length=20)
    salary = models.IntegerField()
    hire_date = models.DateField()


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True, null=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    weight = models.FloatField()
    metal = models.CharField(max_length=30)
    gemstone = models.CharField(max_length=30, blank=True, null=True) # Вставка
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True) # Какой работник обслужил
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    total_price = models.IntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()             # Оценка
    comment = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)