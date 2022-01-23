from django.db import models

# Create your models here.

class student(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)

    def __str__(self):
        return self.FirstName