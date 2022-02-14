from distutils.archive_util import make_zipfile
from django.db import models

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
