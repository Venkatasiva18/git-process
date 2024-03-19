from django.db import models
from django.urls import reverse


class Student(models.Model):
    name = models.CharField(max_length=200)
    rollno = models.IntegerField()
    fee = models.FloatField()
    addr = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.rollno} {self.fee}{self.addr}"


class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.IntegerField()
    email = models.EmailField()


# List View
class College(models.Model):
    college_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    id_number = models.IntegerField()
    fee = models.FloatField()


# DetailView
class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    ceo = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Worker(models.Model):
    eno = models.IntegerField()
    name = models.CharField(max_length=50)
    salary = models.FloatField()
    company = models.ForeignKey(Company, related_name='workers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name




