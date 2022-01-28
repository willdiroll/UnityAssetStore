from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# User info
EMAIL = "lainey.chylik@gmail.com"
PASSWORD = "Password22"

# Set up a headless Firefox browser
op = webdriver.FirefoxOptions()	# Must download the Firefox geckodriver from
								# https://github.com/mozilla/geckodriver/releases
								# Then, move geckodriver into a $PATH directory
								#			e.g. usr/local/bin
op.headless = False		# Can change this to True to avoid opening FireFox window
br = webdriver.Firefox(options = op)

# Navigate to the unity Asset Store login page
URL = 'https://assetstore.unity.com/account/assets'
br.get(URL)

# Locate the login fields
email_field = br.find_element(By.ID, 'conversations_create_session_form_email')
password_field = br.find_element(By.ID, 'conversations_create_session_form_password')
login_button = br.find_element(By.NAME, 'commit')

# Log In
email_field.send_keys(EMAIL)
password_field.send_keys(PASSWORD)
login_button.click()

""" WIP
# Change asset page to show 100 assets
br.find_elements(By.CLASS_NAME, 'Y1yB6')[1].click()
page_size = br.find_elements(By.CLASS_NAME, '_3BlIq')[6]
try:
	page_size.click()
except:
	br.implicitly_wait(2)
	page_size.click()

br.implicitly_wait(10)
"""

# Gather meta-data for each asset on the page
links = []
assets = br.find_elements(By.CLASS_NAME, '_161YN')
for asset in assets:
	br.execute_script('arguments[0].scrollIntoView();', asset)
	
	# ADDED SO SCRAPER WORKS ON MAC
	# Slows scraper down so one element does not obsure another
	timeout = 5
	try:
		present = EC.presence_of_element_located((By.CLASS_NAME, 'asset'))
		WebDriverWait(br, timeout).until(present)
	except TimeoutException:
		print('TIMEOUT')

	try:
		asset.click()
	except:
		br.implicitly_wait(5)
		asset.click()
	links.append(br.find_element(By.CLASS_NAME, '_3UE3J.ZQFsR.auto._2RWe1').get_attribute('href'))
	br.find_element(By.CLASS_NAME, '_1VOoF').click()

# Close the browser
br.quit()

# Print list of links
for link in links:
	print(link)

print(len(links))
