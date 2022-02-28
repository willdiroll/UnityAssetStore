from django.contrib import admin
from .models import Repo, Asset, Label, Category
# Register your models here.
admin.site.register(Repo)
admin.site.register(Asset)
admin.site.register(Label)
admin.site.register(Category)