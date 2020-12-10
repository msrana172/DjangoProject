from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    class Meta:
        db_table = 'employee'

