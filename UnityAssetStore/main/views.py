from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
home_response = """
<h1>Home/Assets Page</h1><br>
<input type="text" name="asset_search_text" id="asset_search_text">
<input type="button" name="asset_search_button" id="asset_search_button" value="Search" onclick="">
<input type="button" name="leave" id="leave" value="Leave" onclick="location.href = 'http://127.0.0.1:8000/join'" style="float: right;">
"""
join_response = """
<input type="button" name="to_credits" id="to_credits" value="Credits" onclick="location.href = 'http://127.0.0.1:8000/credits'">
<h1 align="center">Join a Repo</h1><br>
    <p align="center">
        <label for="class_key">Class Key:</label><br>
        <input type="text" id="class_key" name="class_key"><br>
        <input type="submit" id="submit_key" name="submit_key" value="Join" onclick="location.href = 'http://127.0.0.1:8000/home'">
    </p><br>
    <h3 align="center">Alternatively, <input type="button" name="create_repo" id="create_repo" value="Create!" onclick="location.href = 'http://127.0.0.1:8000/create'"></h3>
"""
create_response = """
<h1>Create Page</h1><br>
Input email to associate with repository:<br>
<input type="text" id="create_email" name="create_email"><br><br>
Input name of repository:<br>
<input type="text" id="create_name" name="create_name"><br><br>
<input type="button" id="new_repo" name="new_repo" value="Start" onclick="location.href = 'http://127.0.0.1:8000/home'">
"""
asset_info_response = """
<h1>Asset Info Page</h1>
"""
edit_asset_response = """
<h1>Edit Asset Page</h1>
"""
add_asset_response = """
<h1>Add Asset Page</h1>
"""
credits_response = """
<h1>Credits Page</h1><br>
<b>Sponsor</b> - Roger Crawfis<br><br>
<b>Developers</b><br>
<table>
    <tr>
        <td>Diego Cepeda</td>
        <td> - Individualized</td>
    </tr>
    <tr>
        <td>Lainey Chylik</td>
        <td> - Database Systems</td>
    </tr>
    <tr>
        <td>Tyler Cingel</td>
        <td> - Information and Computation Assurance</td>
    </tr>
    <tr>
        <td>Will Diroll</td>
        <td> - Individualized</td>
    </tr>
</table>
<br>
This application was written in Python using Django, as well as using SQLite for the backend database.<br>
<input type="button" name="to_join" id="to_join" value="Back to Join Page" onclick="location.href = 'http://127.0.0.1:8000/join'">
"""

def home(response):
    return HttpResponse(home_response)

def join(response):
    return HttpResponse(join_response)

def create(response):
    return HttpResponse(create_response)

def asset_info(response):
    return HttpResponse(asset_info_response)

def edit_asset(response):
    return HttpResponse(edit_asset_response)

def add_asset(response):
    return HttpResponse(add_asset_response)

def credits(response):
    return HttpResponse(credits_response)