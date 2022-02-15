from django.shortcuts import render
from django.http import HttpResponse
from .models import Asset, Repo

def home(response):
    return render(response, "main/homepage.html", {})

def join(response):
    return render(response, "main/join.html", {})

def create(response):
    return render(response, "main/create.html", {})

def asset_info(response):
    return render(response, "main/asset.html", {})

def edit_asset(response):
    return render(response, "main/edit.html", {})

def add_asset(response):
    return render(response, "main/add.html", {})

def credits(response):
    return render(response, "main/credits.html", {})