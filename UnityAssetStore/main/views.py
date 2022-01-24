from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return HttpResponse("<h1>Home/Assets Page</h1>")

def join(response):
    return HttpResponse("<h1>Join Page</h1>")

def create(response):
    return HttpResponse("<h1>Create Page</h1>")

def asset_info(response):
    return HttpResponse("<h1>Asset Info Page</h1>")

def edit_asset(response):
    return HttpResponse("<h1>Edit Asset Page</h1>")

def add_asset(response):
    return HttpResponse("<h1>Add Asset Page</h1>")

def credits(response):
    return HttpResponse("<h1>Credits Page</h1>")