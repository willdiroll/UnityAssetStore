from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("join/", views.join, name="join"),
    path("create/", views.create, name="create"),
    path("asset_info/", views.asset_info, name="asset_info"),
    path("edit_asset/", views.edit_asset, name="edit_asset"),
    path("add_asset/", views.add_asset, name="add_asset"),
    path("credits/", views.credits, name="credits")
]