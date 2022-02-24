from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import main.scraper as scraper

def home(response):
    if response.method == 'POST' and 'run_scraper' in response.POST:
        repo_id = response.POST.get('create_email')
        repo_name = response.POST.get('create_name')
        repo_password = response.POST.get('create_password')
        scraper.scrape(repo_id, repo_name, repo_password)

    all_assets = Asset.objects.all()
    return render(response, "main/homepage.html", {'all_assets': all_assets})

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
