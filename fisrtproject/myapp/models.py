from statistics import mode
from turtle import title
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

class Student(models.Model):
    studentname = models.CharField(max_length=15)
    studentclass = models.CharField(max_length=10)
    studentbdate = models.DateField('birth date')
    studentage = models.IntegerField(max_length=2)
    studenthobby = models.CharField(max_length=10)
    studentfavsub = models.CharField(max_length=10)