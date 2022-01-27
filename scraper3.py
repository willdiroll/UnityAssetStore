from requests_html import HTML
import mechanize
from bs4 import BeautifulSoup

# User and webpage data
URL = 'https://assetstore.unity.com/account/assets'
EMAIL = 'lainey.chylik@gmail.com'
PASSWORD = 'Password22'

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

# Start a Request-HTML session
raw_html = BeautifulSoup(asset_store, 'html.parser')
session = HTML(html = raw_html.prettify())
session.render()