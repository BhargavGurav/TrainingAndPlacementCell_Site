from django.db import models
from django.contrib.auth.models import User

class Mou(models.Model):
    title = models.CharField(max_length=100)
    mou = models.FileField(upload_to='Mou')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class PlacementReport(models.Model):
    title = models.CharField(max_length=100)
    report = models.FileField(upload_to='Placementreport')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Broucher(models.Model):
    title = models.CharField(max_length=100)
    broucher = models.FileField(upload_to='broucher')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    passing_year = models.IntegerField()
    branch = models.CharField(max_length=50)
    cgpa = models.FloatField()
    prn = models.CharField(max_length=8)
    resume = models.FileField(upload_to='Resume')

    def __str__(self):
        return self.name

class Query(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    