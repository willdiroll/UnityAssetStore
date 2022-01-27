import requests_html
import requests
import mechanize
from bs4 import BeautifulSoup

# User and webpage data
URL = 'https://assetstore.unity.com/account/assets'
LOGIN_URL = 'https://id.unity.com/en/conversations/1fec57c6-ea1e-423d-960a-25d837306360012f'
EMAIL = 'lainey.chylik@gmail.com'
PASSWORD = 'Password22'
payload = {
	'utf8' : '✓',
	'_method' : 'put',
	'authenticity_token' : 'mh3k3btVczByEZwNtkLYYrJRLosdFUy9ey1+XWTmPO+So/tRP77mXWLlyocBHG1zQ/ikatPMStMkLKj3oZmVtQ==',
	'conversations_create_session_form[email]' : EMAIL,
	'conversations_create_session_form[password]' : PASSWORD,
	'conversations_create_session_form[remember_me]' : 'false',
	'commit' : 'Sign in'
}

"""
with requests_html.HTMLSession() as session:
	post = session.post(LOGIN_URL, data=payload)
	print(post.text)
"""

# Set up a mechanize Browser object (for submitting login form)
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.set_handle_refresh(False)
br.open(URL)

# Find the login form
br.select_form(id = 'new_conversations_create_session_form')

# Enter login fields
br.controls[3].value = EMAIL
br.controls[4].value = PASSWORD
br.submit()

# Redirect to the asset store
asset_store = br.follow_link( br.links()[0])
with requests_html.HTMLSession() as session:
	print(dir(br.links()[0]))

"""
# Start a Request-HTML session
raw_html = BeautifulSoup(asset_store, 'html.parser')
session = HTML(html = raw_html.prettify())
for i in session.links:
	print(i)
"""