
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# A function that breaks down the given link to access the asset's title, ID, and corresponding categories
def get_link_info(link):
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
wait = WebDriverWait(br, 5)

# Navigate to the unity Asset Store login page
URL = 'https://assetstore.unity.com/account/assets'
br.implicitly_wait(5)
br.get(URL)

# Locate the login fields
email_field = br.find_element(By.ID, 'conversations_create_session_form_email')
password_field = br.find_element(By.ID, 'conversations_create_session_form_password')
login_button = br.find_element(By.NAME, 'commit')

# Log In
email_field.send_keys(EMAIL)
password_field.send_keys(PASSWORD)
login_button.click()

# Entered the 'My Asset Page'
# Show 100 assets per page
br.find_elements(By.CLASS_NAME, 'Y1yB6')[1].click()
page_size = br.find_elements(By.CLASS_NAME, '_3BlIq')[6]
wait.until(EC.element_to_be_clickable(page_size)).click()
time.sleep(2)

# Loop thru Asset pages
has_next_page = True
links = []
while has_next_page:

	# Loop thru assets on the current page
	assets = br.find_elements(By.CLASS_NAME, '_161YN')
	# Scroll to top of the page to begin execution 
	br.execute_script("window.scrollTo(0, 0);")

	asset_blocks = br.find_elements(By.CLASS_NAME, '_1QlFG')
	for blocks in asset_blocks:
		names = blocks.find_elements(By.CLASS_NAME, '_161YN._30Ec_')
		for name in names:
			print(name.text)
		elements = blocks.find_elements(By.CLASS_NAME, 'le_6J')
		for element in elements:
			print(element.text)
	
	for asset in assets:
		br.execute_script('arguments[0].scrollIntoView();', asset)
		time.sleep(1)
		wait.until(EC.element_to_be_clickable(asset)).click()
		
		"""" label testing, prints all of the labels present on the page
		labels = br.find_elements(By.CLASS_NAME, 'le_6J')
		for label in labels:
			print(label.text)
		"""

		links.append(br.find_element(By.CLASS_NAME, '_3UE3J.ZQFsR.auto._2RWe1').get_attribute('href'))

		link = br.find_element(By.CLASS_NAME, '_3UE3J.ZQFsR.auto._2RWe1').get_attribute('href')

		br.find_element(By.CLASS_NAME, '_1VOoF').click()

	# Check for next page
	next_page = br.find_element(By.CLASS_NAME, '_3UE3J.auto._3wJlw.F35ws')
	has_next_page = next_page.is_enabled()

	# Click next page button if it is enabled
	if has_next_page:
		wait.until(EC.element_to_be_clickable(next_page)).click()

# Close the browser
br.quit()

# Print list of links and their corresponding information
for link in links:
	print(link)
	info = get_link_info(link)
	categories = info[:len(info) - 2]
	print("Title: "+info[len(info) - 1]+ ", Asset ID: "+info[len(info) -2]+ ", Categories: "+ ', '.join(map(str, categories)))

print(len(links))


