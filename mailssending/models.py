from django.db import models

# Create your models here.
class Student(models.Model):
    subject=models.CharField(max_length=20)
    email=models.EmailField()
    messages=models.CharField(max_length=299)
