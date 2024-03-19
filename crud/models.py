from django.db import models
from django.urls import reverse


class Beer(models.Model):
    name = models.CharField(max_length=120)
    taste = models.CharField(max_length=120)
    color = models.CharField(max_length=120)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Employeeinfo(models.Model):
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length=64)
    emp_sal = models.FloatField()
    emp_addr = models.CharField(max_length=256)


