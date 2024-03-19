from django.db import models


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=200)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=200)

    def __str__(self):
        return 'Employee object with eno:+str(self.no)'



