from distutils.archive_util import make_zipfile
from django.db import models
import datetime
import django

class Repo(models.Model):
    Key = models.IntegerField(default=1, unique=True)
    Name = models.CharField(max_length=100)
    Identifier = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
    class Meta:
        app_label = 'main'

class Asset(models.Model):
    class Meta:
        app_label = 'main'
    AID = models.IntegerField(default=0, unique=True)
    AssetName = models.CharField(max_length=100)
    AssetLink = models.CharField(max_length=100)
    LastUpdated = models.DateField(default= django.utils.timezone.now)
    VersionNum = models.CharField(max_length=100)
    ImgLink = models.CharField(max_length=100)
    Repos = models.ManyToManyField(Repo)

    def __str__(self):
        return self.AssetName

class Label(models.Model):
    class Meta:
        app_label = 'main'
    LabelName = models.CharField(max_length=100, unique=True)
    Assets = models.ManyToManyField(Asset)
    
    def __str__(self):
        return self.LabelName

class Category(models.Model):
    class Meta:
        app_label = 'main'
    CategoryName = models.CharField(max_length=100, unique=True)
    Assets = models.ManyToManyField(Asset)
    
    def __str__(self):
        return self.CategoryName

