from distutils.archive_util import make_zipfile
from django.db import models

# Create your models here.
#
#class student(models.Model):
#    FirstName = models.CharField(max_length=100)
#    LastName = models.CharField(max_length=100)
#    Email = models.CharField(max_length=100)
#
#    def __str__(self):
#        return self.FirstName

#class student_class(models.Model):
#    Email = models.CharField(max_length=100) #add FK to students
#    AID = models.CharField(max_length=100) #add FK to asset_info
#
#    def __str__(self):
#        return self.Email


class Asset(models.Model):
    AID = models.IntegerField(primary_key=True)
    AssetName = models.CharField(max_length=100)
    AssetLink = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Version = models.CharField(max_length=100)
    #MetaData = 
    ImgLink = models.CharField(max_length=100)
    Keywords = models.CharField(max_length=200)

    def __str__(self):
        return self.AssetName

class Repo(models.Model):
    RepoKey = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Identifier = models.CharField(max_length=100)
    AID = models.ForeignKey(Asset, default=None, on_delete=models.CASCADE)

#class professor(models.Model):
#    ProfFirstName = models.CharField(max_length=100)
#    ProfLastName = models.CharField(max_length=100)
#    ProfEmail = models.CharField(max_length=100)
#
#    def __str__(self):
#        return self.ProfFirstName

#class class_info(models.Model):
#    ClassKey = models.CharField(max_length=100)
#    ProfEmail = models.CharField(max_length=100) #Add FK back to professors model
#    ClassName = models.CharField(max_length=100)
#
#    def __str__(self):
#        return self.ClassName

#class class_asset(models.Model):
#   ClassKey = models.CharField(max_length=100) #add FK to class_info
#    AID = models.CharField(max_length=100) #add FK to asset_info

#    def __str__(self):
#        return self.ClassKey

