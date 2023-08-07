from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    message=models.CharField(max_length=300)

class CustomerDetail_Order(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    choice = (
        ("pizza", "pizza"),
        ("burger","burger"),
        ("hotdog","hotdog"),
        ("muffins","muffins"),
        )
    food = models.CharField(blank=False, choices=choice, max_length=10,default="muffins")
    num=models.IntegerField()

    

    
    

