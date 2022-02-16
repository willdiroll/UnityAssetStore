from distutils.archive_util import make_zipfile
from django.db import models
import datetime

class Repo(models.Model):
    RepoKey = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Identifier = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Asset(models.Model):
    AID = models.IntegerField(primary_key=True)
    AssetName = models.CharField(max_length=100)
    AssetLink = models.CharField(max_length=100)
    LastUpdated = models.DateField(default=datetime.date.today())
    VersionNum = models.CharField(max_length=100)
    ImgLink = models.CharField(max_length=100)
    RepoKey = models.ForeignKey(Repo, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.AssetName

class Label(models.Model):
    AID = models.ForeignKey(Asset, default=None, on_delete=models.CASCADE)
    LabelName = models.CharField(max_length=100)

    def __str__(self):
        return self.AssetName

class Category(models.Model):
    AID = models.ForeignKey(Asset, default=None, on_delete=models.CASCADE)
    CategoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.CategoryName

