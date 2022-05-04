from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    duration= models.IntegerField()
    author_name = models.CharField(max_length=100)
