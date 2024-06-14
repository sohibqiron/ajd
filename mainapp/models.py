from django.db import models

# Create your models here.

COUNTRY_CHOICE = [
    ("Uzbekiston","Uzbekiston"),
    ("Qozogiston","Qozogiston"),
    ("Tojikiston","Tojikiston",)
]

class Employee(models.Model):
    
    CITY_CHOICE = [
        ("TASHKENT","TASHKENT")
    ]
    
    full_name = models.CharField(max_length=65)
    birth_date = models.DateField()
    country = models.CharField(max_length=10,choices=COUNTRY_CHOICE,default="Uzbekiston")
    city = models.CharField(max_length=8,choices=CITY_CHOICE,default="TASHKENT")
    address = models.CharField(max_length=65)
    salary = models.FloatField()
    avatar = models.ImageField(upload_to='employee/')
    specialty = models.CharField(max_length=55)
    descriptions = models.TextField()
    
    
    def __str__(self):
        return self.full_name
    
    def final_salary(self):
        one_per = self.salary / 100
        ten_per = one_per * 10
        final_salary = self.salary - ten_per
        return final_salary
    
class Products(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    end_date = models.DateField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    
    def total_amounts(self):
        total_amounts = self.price * self.quantity
        return total_amounts
    
    
    
class Noutbook(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    end_date = models.DateField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    
    def total_amounts(self):
        total_amounts = self.price * self.quantity
        return total_amounts
    