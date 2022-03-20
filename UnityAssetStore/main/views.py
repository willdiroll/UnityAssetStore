from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import main.scraper as scraper

def home(response):
    if response.method == 'POST' and 'create_repo' in response.POST:
        unity_email = response.POST.get('create_email')
        unity_password = response.POST.get('create_password')
        repo_name = response.POST.get('create_name')

        filterargs = {'Identifier': unity_email, 'Name': repo_name }
        if not Repo.objects.filter(**filterargs).exists():
            scraper.scrape(repo_name, unity_email, unity_password)

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
