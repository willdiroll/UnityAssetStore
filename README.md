# HOW TO USE (Windows):


## SET UP

1. Set up Git

	Go to https://git-scm.com/download/win to download/install latest build for Windows
	Follow the installer default steps
		
		Configure Git with your identity in a command prompt (cmd.exe):
		$ git config --global user.name "John Doe"
		$ git config --global user.email johndoe@example.com
	
2. Install the Heroku CLI

	Go to https://cli-assets.heroku.com/heroku-x64.exe to download/install latest build for Windows (x64)
	Follow the installer default steps
		
		You should now be able to use the 'heroku' command on cmd.exe
		
		Verify your installation with
		$ heroku --version
		
3. Clone the app from Heroku

	If you do not have a Heroku account, create one at https://signup.heroku.com/login
		
		Login to Heroku from Heroku CLI on cmd.exe with
		$ heroku login
		
		In cmd.exe, navigate to a directory you would like to place the app in, then use
		$ heroku git:clone -a roly-united
		
		** NOTE: We will need to add your Heroku account as a Collaborator on our app before you can clone it!
		
		You should now have a local copy of the app!
		
4. Install Python3

	Go to https://www.python.org/downloads/windows/ to download/install latest build for Windows
	- Recommended: Windows Installer (64-bit)
	- On the installer wizard: check "Add Python 3.10 to PATH"

			Verify your installation with 
			$ python -V
		
		
		
5. Install Python modules and Chrome files (Install these if you haven't already)
	- Selenium:

			$ pip install selenium
	- Django:

			$ pip install django
	- Django-Heroku:

			$ pip install django-heroku
	- Google Chrome Browser:

			Go to https://www.google.com/chrome/
	- Chromedriver

			1. Go to https://chromedriver.chromium.org/home
			2. Go to "latest stable release: " > "chromedriver_win32.zip"
			3. Unzip "chromedriver_win32.zip" into a directory that is easily accessible
			4. Add that directory to your PATH variable:
				- Press WIN+S to launch Windows Search
				- Type "environ..." and select "Edit the system environment variables"
				- Select "Environment Variables..."
				- Select the "Path" variable in the top menu
				- Select "New" (**important... if you don't select this, it will replace an entry)
				- Select "Browse..." and select the directory containing your "chromedriver.exe" file
				
6. Install Postgres

		1. Go to https://www.postgresql.org/download/windows/ to download/install latest build for Windows
		2. Select "Download the installer"
		3. Download the latest version for Windows x86-64
		4. Follow the instructions on the installer wizard
			- Use any superuser password you'd like (** Remember this for next step)
			- Use the default port number

7. Create a Postgres Database and User


		1. Press WIN+S to launch Windows Search
		2. Search "psql" and select it to open the Postgresql Shell
		3. Click Enter for "Server", "Datebase", "Port", and "Username"
		4. Enter the password you specified in Step 6.
			** You should now be in the psql shell
		5. Now, enter the following commands in the command prompt:
			postgres=# CREATE DATABASE uas;
			postgres=# CREATE USER lainey WITH PASSWORD 'test';
			** Use the variable names specified above. Do not use a different database name, user name, or password.
		
8. Migrate tables/relations to the Database

		1. In cmd.exe, navigate to roly-united/UnityAssetStore/main/
		2. In cmd.exe navigate to roly-united/UnityAssetStore
		3. Migrate the relations in cmd.exe:
			$ python manage.py makemigrations
			$ python manage.py migrate
		
		Expected Output for 1st time running:
		$ Operations to perform:
		$ 	Apply all migrations: admin, auth, contenttypes, main, sessions
		$ Running migrations:
		$	Applying contenttypes.0001_initial... OK
		$	Applying auth.0001_initial... OK
		$	Applying admin.0001_initial... OK
		$	Applying admin.0002_logentry_remove_auto_add... OK
		$	Applying admin.0003_logentry_add_action_flag_choices... OK
		$	Applying contenttypes.0002_remove_content_type_name... OK
		$	Applying auth.0002_alter_permission_name_max_length... OK
		$	Applying auth.0003_alter_user_email_max_length... OK
		$	Applying auth.0004_alter_user_username_opts... OK
		$	Applying auth.0005_alter_user_last_login_null... OK
		$	Applying auth.0006_require_contenttypes_0002... OK
		$	Applying auth.0007_alter_validators_add_error_messages... OK
		$	Applying auth.0008_alter_user_username_max_length... OK
		$	Applying auth.0009_alter_user_last_name_max_length... OK
		$	Applying auth.0010_alter_group_name_max_length... OK
		$	Applying auth.0011_update_proxy_permissions... OK
		$	Applying auth.0012_alter_user_first_name_max_length... OK
		$	Applying main.0001_initial... OK
		$	Applying main.0002_alter_asset_assetlink_alter_asset_assetname_and_more... OK
		$	Applying sessions.0001_initial... OK
		
		*** You should now be prepared to use the app!
	
## POPULATE THE DATABASE WITH THE WEB SCRAPER

Run the scraper:

	1. In cmd.exe navigate to roly-united/UnityAssetStore/  
	2. Run the scraper from cmd.exe:
		$ python scraper.py
		
Expected output:

	C:\Users\Diego\Desktop\roly-united\UnityAssetStore>python scraper.py
	running scraper.py...

	------------------------------------

	Provide Unity login info: (leave Email or Password blank to skip)
	Email: *****@example.com
	Password: 

	Select scraping mode (enter a number):
	0. Exit
	1. All:              scrapes all assets (recommended for accounts w/ <200 assets)
	2. Recently Added:   scrapes up until asset that is already saved
	3. Per Page:         scrapes all assets on a certain page (100 assets per page)
	<user input 0-3>
	
	------------------------------------

	Do you want to scrape only 'Paid' assets? (y/n) <user input y/n>
	(Note: all assets will be scraped if you have no assets labeled 'Paid')

	------------------------------------
	
If chose menu option (0):
	
	$ Exiting
	
If chose menu option (1):
	
	$ Scraping all (Paid) assets from your Unity account!

	$ DevTools listening on ws://127.0.0.1:61989/devtools/browser/59b5d5ca-4462-4356-8aa8-b6d4fd32cb5d
	$ Go to 'https://assetstore.unity.com/account/assets'
	$ Log in
	$ Set page size to 100 assets
	$ 
	$ You have <A> assets across <P> pages.
	$ Waiting 5 seconds for assets on the page to load...
	$ added assets:  1
	$ added assets:  2
	$ added assets:  3
	$ ...
	$ added assets: <# of assets TOTAL>
	$ Finished!
	
If chose menu option (2):

	$ Scraping your most recently added (Paid) assets!

	$ DevTools listening on ws://127.0.0.1:61989/devtools/browser/59b5d5ca-4462-4356-8aa8-b6d4fd32cb5d
	$ Go to 'https://assetstore.unity.com/account/assets'
	$ Log in
	$ Set page size to 100 assets
	$ 
	$ You have <A> assets across <P> pages.
	$ Waiting 5 seconds for assets on the page to load...
	$ added assets:  1
	$ added assets:  2
	$ added assets:  3
	$ ...
	$ added assets: <# of assets RECENTLY ADDED>
	$ Update complete!
	
If chose menu option (3):

	$ Scraping all (Paid) assets from a certain page!
	$
	$ DevTools listening on ws://127.0.0.1:57361/devtools/browser/d78adc6c-b477-47cc-b7f6-df5aefc441c9
	$ Go to 'https://assetstore.unity.com/account/assets'
	$ Log in
	$ Set page size to 100 assets
	$
	$ You have <A> assets across <P> pages.
	$
	$ ------------------------------------
	$ 
	$ Please enter a valid page number from 1 to <P>
	$ Enter the page # you would like to scrape: <user input>
	$ Reaching page 2
	$ Waiting 5 seconds for assets on the page to load...
	$ added assets:  1
	$ added assets:  2
	$ added assets:  3
	$ ...
	$ added assets:  <# of assets on the page>
	$ Finished!
	
If chose invalid menu option:

	Please select a valid menu option (enter a number)
	0. Exit
	1. All:              scrapes all assets
	2. Recently Added:   scrapes up until asset that is already saved
	
## CHECK WHAT POPULATED INTO THE DATABASE (OPTIONAL)

	1. In cmd.exe, navigate to roly-united/UnityAssetStore
	2. Create a superuser for the locally-hosted website in cmd.exe:
		$ python manage.py createsuperuser
	3. Follow the command line prompts to create super user credentials
	4. Run localhost server in cmd.exe:
		$ python manage.py runserver
	5. In a browser, go to the localhost URL (by default, http://127.0.0.1:8000/)
	6. Go to /admin/ page (e.g. http://127.0.0.1:8000/admin/), and login using the credentials you specified before
	
	*** From here, you can view all the assets added in "Assets" and delete any you choose. 
		  

## CREATE A DATABASE DUMP FILE:

	1. In cmd.exe, navigate to a directory you would like to place the dump file in.
	2. Generate a database dump file using the below command in cmd.exe:
		$ pg_dump -Fc --no-acl --no-owner -h <HOST> -U <USER> -d <DB_NAME> -f uas_db.dump
	
		*** For our app, this is the literal command:
		$ pg_dump -Fc --no-acl --no-owner -h localhost -U lainey -d uas -f uas_db.dump 
		$ password: test
    			
## IMPORT DUMP FILE INTO HEROKU APP:

	1. Create/Login to your AWS Account.
	2. In the search bar saying "Search for services, features...", search for "S3" and select the result "S3"
	3. (Skip if already created a bucket) Select "Create bucket"
	4. (Skip if already created a bucket) Under "Bucket name" use any name you wish. Use the default selections for the other settings
	5. Upload your dump file (e.g. "uas_db.dump") into a bucket
	6. Select the checkbox next to the dump file in the bucket, then select "Actions" > "Share with a presigned URL"
	7. In cmd.exe, navigate to your roly-united directory. Then run the below command:
		$ heroku pg:backups:restore --app <APP_NAME> --confirm <APP_NAME> "<GENERATED_URL>"
	
		*** For our app, this is the literal command:
		$ heroku pg:backups:restore --app roly-united --confirm roly-united "<GENERATED_URL>"
	
## ACCESS THE REMOTELY HOSTED APP

	Go to https://roly-united.herokuapp.com/
	
	Features on the app include:
	- Sorting (by Asset Name or by Date Last Updated)
	- Filtering (via a set of Categories and Labels)
		- The filtering action is characterized by the following:
			{ c1 OR c2 OR ... OR cN } AND { l1 AND l2 AND ... AND lN } or
			{ c1 OR c2 OR ... OR cN } AND { l1 OR l2 OR ... OR lN }
	- Asset Pagination
	
## UPDATE YOUR APP

There are 2 ways you can update the app:

Method 1: Clone the app from Heroku again (same as SET UP > Step 3.)

	1. Login to Heroku from Heroku CLI on cmd.exe with
		$ heroku login
	2. In cmd.exe, navigate to a directory you would like to place the app in, then use
		$ heroku git:clone -a roly-united
		
	NOTE: This creates a new roly-united directory on your machine, so you likely want to delete your old one to avoid confusion!

Method 2: Pull from the remote repo and overwrite local changes

	1. In cmd.exe, navigate to your roly-united directory
	2. Revert any local changes you may have made using the below cmd:
		$ git restore .
	3. Pull changes from the remote master branch:
		$ git pull
		
	NOTE: This does NOT create a new directory.

## SHARING THE APP WITH FUTURE DEVELOPERS

	1. Login to your Heroku account on https://id.heroku.com/login
	2. Select the app to enter its Dashboard
	3. Go to the 'Access' Tab
	4. Click on 'Add collaborator' and enter the email associated with your developer's Heroku account
	
	** The Heroku users added as Collaborators can now access the codebase via a git clone (see SET UP steps 2, 3)
	
## FUTURE CONSIDERATIONS/IMPROVEMENTS

	- On the web app, split the 'Categories' and 'Labels' lists into different scrollboxes.
	- Expand upon 'Repo' functionality
		- Allow users to create their own Asset pages which they can share via access codes
	- Create a more user-friendly interface for updating assets (web scraping). E.g:
		- Progress bar
		- Graphical UI
		- Windows Batch Files (for executing scraper and other command-line actions)
	- Make web scraper more consistent
