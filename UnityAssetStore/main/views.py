from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import main.scraper as scraper

def home(response):
    filter_categories = []
    filter_labels = []
    if response.method == 'POST' and 'create_repo' in response.POST:
        unity_email = response.POST.get('create_email')
        unity_password = response.POST.get('create_password')
        repo_name = response.POST.get('create_name')

        filterargs = {'Identifier': unity_email, 'Name': repo_name }
        if not Repo.objects.filter(**filterargs).exists():
            scraper.scrape(repo_name, unity_email, unity_password)

    elif response.method == 'POST' and 'filter_assets' in response.POST:
        filter_categories = response.POST.getlist('categories[]')
        filter_labels = response.POST.getlist('labels[]')

    all_assets = Asset.objects.all()
    all_labels = Label.objects.all()
    all_categories = Category.objects.all()

    sort_labels = []
    sort_categories = []
    for c in all_categories:
        sort_categories.append(c.CategoryName)
    for l in all_labels:
        sort_labels.append(l.LabelName)

    if len(filter_categories) > 0 or len(filter_labels) > 0:
        filter_assets = []
        for c in filter_categories:
            query_set = Category.objects.get(CategoryName = c).Assets.all()
            for ele in query_set:
                if not ele in filter_assets: filter_assets.append(ele)

        for l in filter_labels:
            query_set = Label.objects.get(LabelName = l).Assets.all()
            for ele in query_set:
                if not ele in filter_assets: filter_assets.append(ele)

        all_assets = filter_assets

    return render(response, "main/homepage.html", {
        'all_assets': all_assets, 
        'all_labels': sorted(sort_labels), 
        'all_categories': sorted(sort_categories),
        'filter_categories': filter_categories,
        'filter_labels': filter_labels})

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
