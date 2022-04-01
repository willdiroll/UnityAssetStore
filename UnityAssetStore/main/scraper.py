from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import warnings
import datetime

import os
import sys

import django

from django.conf import settings
if not settings.configured:
	settings.configure(
		DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2',
		DATABASE_NAME = 'uas',
		DATABASE_USER = 'lainey',
		DATABASE_PASSWORD = 'test',
		DATABASE_HOST = 'localhost',
		DATABASE_PORT = '',
	)

django.setup()

os.environ["DJANGO_SETTINGS_MODULE"] = 'UAS.settings'

sys.path.append('..')
from main.models import *
print("1")

# Breaks down the given link to access the asset's title, ID, and corresponding categories
def get_link_info(link):
	print("info")
    # Removes the part of link that is uniform throughout
	trimmed_link = link[38:]

    # Puts all of the categories at beginning of info array
	info = trimmed_link.split('/')
	title_id = info[len(info) - 1]
	info.remove(title_id)
	title_id = title_id.split('-')
	id = title_id[len(title_id) - 1]

	# ID added to info[len(info) - 2]
	info.append(id)
	title_id.remove(id)
	title = " ".join(title_id)

	# Title added to info[len(info) - 1]
	info.append(title)

	return info

# Parses the string representation of dates (MON DAY, YEAR) into a Date object
def parse_date(str_date):
	print("date")
	split = str_date.split(' ')
	str_month = split[0]
	day = split[1].replace(',', '')
	year = split[2]

	parse_month = {
		'Jan' : 1,
		'Feb' : 2,
		'Mar' : 3,
		'Apr' : 4,
		'May' : 5,
		'Jun' : 6,
		'Jul' : 7,
		'Aug' : 8,
		'Sep' : 9,
		'Oct' : 10,
		'Nov' : 11,
		'Dec' : 12,
	}
	month = parse_month.get(str_month, 0)

	return datetime.date(int(year), int(month), int(day))

# Initializes the web driver settings used for scraping the web site
def webdriver_settings():
	print("webdriver")
	# Set up a Firefox webdriver options
	op = webdriver.FirefoxOptions()	# Must download the Firefox geckodriver from
									# https://github.com/mozilla/geckodriver/releases
									# Then, move geckodriver into a $PATH directory
									#			e.g. usr/local/bin
	op.headless = True		# Can change this to True to avoid opening FireFox window

	# Miscellaneous settings to make the webdriver run a bit faster
	warnings.filterwarnings("ignore", category=DeprecationWarning) 
	profile = webdriver.FirefoxProfile()
	profile.set_preference("network.http.pipelining", True)
	profile.set_preference("network.http.proxy.pipelining", True)
	profile.set_preference("network.http.pipelining.maxrequests", 8)
	profile.set_preference("content.notify.interval", 500000)
	profile.set_preference("content.notify.ontimer", True)
	profile.set_preference("content.switch.threshold", 250000)
	profile.set_preference("browser.cache.memory.capacity", 65536) 				# Increase the cache capacity.
	profile.set_preference("browser.startup.homepage", "about:blank")
	profile.set_preference("reader.parse-on-load.enabled", False) 				# Disable reader, we won't need that.
	profile.set_preference("browser.pocket.enabled", False) 					# Duck pocket too!
	profile.set_preference("loop.enabled", False)
	profile.set_preference("browser.chrome.toolbar_style", 1) 					# Text on Toolbar instead of icons
	profile.set_preference("browser.display.show_image_placeholders", False) 	# Don't show thumbnails on not loaded images.
	profile.set_preference("browser.display.use_document_colors", False) 		# Don't show document colors.
	profile.set_preference("browser.display.use_document_fonts", 0) 			# Don't load document fonts.
	profile.set_preference("browser.display.use_system_colors", True) 			# Use system colors.
	profile.set_preference("browser.formfill.enable", False) 					# Autofill on forms disabled.
	profile.set_preference("browser.helperApps.deleteTempFileOnExit", True) 	# Delete temprorary files.
	profile.set_preference("browser.shell.checkDefaultBrowser", False)
	profile.set_preference("browser.startup.homepage", "about:blank")
	profile.set_preference("browser.startup.page", 0) 							# blank
	profile.set_preference("browser.tabs.forceHide", True) 						# Disable tabs, We won't need that.
	profile.set_preference("browser.urlbar.autoFill", False) 					# Disable autofill on URL bar.
	profile.set_preference("browser.urlbar.autocomplete.enabled", False) 		# Disable autocomplete on URL bar.
	profile.set_preference("browser.urlbar.showPopup", False) 					# Disable list of URLs when typing on URL bar.
	profile.set_preference("browser.urlbar.showSearch", False) 					# Disable search bar.
	profile.set_preference("extensions.checkCompatibility", False) 				# Addon update disabled
	profile.set_preference("extensions.checkUpdateSecurity", False)
	profile.set_preference("extensions.update.autoUpdateEnabled", False)
	profile.set_preference("extensions.update.enabled", False)
	profile.set_preference("general.startup.browser", False)
	profile.set_preference("plugin.default_plugin_disabled", False)

	# Add settings to the webdriver options object
	op.profile = profile

	return op

def add_to_database(repo_name, unity_email, assets):
	print("add")
	# Create new repo in database
	new_repo = Repo.objects.create(
		Key = Repo.objects.count() + 1,
		Name = repo_name,
		Identifier = unity_email)	

	# Loop thru each scraped asset
	for a in assets:

		# Create Asset
		if not Asset.objects.filter(AID=a['id']).exists():
			# If asset doesn't exist yet, add it
			asset = Asset.objects.create(
				AID = a['id'],
				AssetName = a['title'],
				AssetLink = a['link'],
				LastUpdated = a['last updated'],
				VersionNum = a['version'],
				ImgLink = a['image'])
		else:
			# Else, retrieve existing asset
			asset = Asset.objects.get(AID=a['id'])

		# Add Asset -> Repo
		asset.Repos.add(new_repo) 

		# Add Categories -> Asset
		for c in a['categories']:
			if not Category.objects.filter(CategoryName=c).exists():
				# If category doesn't exist yet, add it
				category = Category.objects.create(CategoryName=c)
			else:
				category = Category.objects.get(CategoryName=c)
			category.Assets.add(asset)

		# Add Labels -> Asset
		for l in a['labels']:
			if not Label.objects.filter(LabelName=l).exists():
				# If category doesn't exist yet, add it
				label = Label.objects.create(LabelName=l)
			else:
				label = Label.objects.get(LabelName=l)
			label.Assets.add(asset)


def scrape(repo_name, unity_email, unity_password):
	print("scrape")
	# Web driver
	op = webdriver_settings()
	br = webdriver.Firefox(options = op)
	wait = WebDriverWait(br, 5)

	"""
	# User info
	EMAIL = "lainey.chylik@gmail.com"
	PASSWORD = "Password22"
	"""

	# Navigate to the unity Asset Store login page
	URL = 'https://assetstore.unity.com/account/assets'
	br.implicitly_wait(1)
	br.get(URL)

	# Locate the login fields
	email_field = br.find_element(By.ID, 'conversations_create_session_form_email')
	password_field = br.find_element(By.ID, 'conversations_create_session_form_password')
	login_button = br.find_element(By.NAME, 'commit')

	# Log In
	email_field.send_keys(unity_email)
	password_field.send_keys(unity_password)
	login_button.click()

	# Entered the 'My Asset Page'
	# Show 100 assets per page
	br.find_elements(By.CLASS_NAME, 'Y1yB6')[1].click()
	page_size = br.find_elements(By.CLASS_NAME, '_3BlIq')[6]
	wait.until(EC.element_to_be_clickable(page_size)).click()
	time.sleep(2)

	# Loop thru Asset pages
	has_next_page = True
	assets = []
	while has_next_page:

		# Find all asset div containers on the page
		asset_divs = br.find_elements(By.CLASS_NAME, '_1QlFG')

		# Scroll to top of the page to begin execution 
		br.execute_script('window.scrollTo(0, 0);')

		i = 0
		# Loop thru all asset div containers
		for asset_div in asset_divs:

			# Asset title
			asset = asset_div.find_element(By.CLASS_NAME, '_161YN')

			# Asset labels
			labels = asset_div.find_elements(By.CLASS_NAME, 'le_6J')

			# Asset thumbnail image link
			img = asset_div.find_element(By.CLASS_NAME, '_12z5H').get_attribute('style')
			img = img.split('//')[1]
			img = img.split('\"')[0]

			# Click on the asset to open window
			br.execute_script('arguments[0].scrollIntoView();', asset)
			try:
				wait.until(EC.element_to_be_clickable(asset)).click()
			except:
				time.sleep(1)
				wait.until(EC.element_to_be_clickable(asset)).click()
			
			# Get asset info
			link = br.find_element(By.CLASS_NAME, '_3UE3J.ZQFsR.auto._2RWe1').get_attribute('href')
			version_info = asset_div.find_element(By.CLASS_NAME, '_4ROtP').text
			str_last_updated = version_info.split(' • ')[0].replace('Last updated: ', '')
			last_updated = parse_date(str_last_updated)
			version_num = version_info.split(' • ')[1].replace('Version: ', '')
			info = get_link_info(link)
			title = asset.text
			asset_id = info[len(info) - 2]
			categories = info[:len(info) - 2]
			label_list = []
			for label in labels:
				label_list.append(label.text)

			# Compile asset info
			assets.append( { 
				'title' : title, 
				'id' : asset_id,
				'categories' : categories,
				'labels' : label_list,
				'link' : link,
				'version' : version_num,
				'last updated' : last_updated,
				'image' : img } ) 

			

			# Close asset window
			br.find_element(By.CLASS_NAME, '_1VOoF').click()

			# TESTING PURPOSES
			i = i + 1
			if i == 5:
				break

		# Check for next page
		next_page = br.find_element(By.CLASS_NAME, '_3UE3J.auto._3wJlw.F35ws')
		has_next_page = next_page.is_enabled()

		has_next_page = False

		# Click next page button if it is enabled
		if has_next_page:
			wait.until(EC.element_to_be_clickable(next_page)).click()

	# Close the browser
	br.quit()

	add_to_database(repo_name, unity_email, assets)
	
# scrape("test_repo", "lainey.chylik@gmail.com", "Password22")