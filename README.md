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
		2. Edit scraper.py:
			Scroll to the bottom and make sure the call to "scrape()" is commented out
				e.g. ' #scrape("test_repo", "email@gmail.com", "password") '
				NOT  ' scrape("test_repo", "email@gmail.com", "password") '
		3. In cmd.exe navigate to roly-united/UnityAssetStore
		4. Migrate the relations in cmd.exe:
			$ python manage.py makemigrations
			$ python manage.py migrate
		
		Should output:
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
		
		**You should now be prepared to use the app!
	
## POPULATE THE DATABASE WITH THE WEB SCRAPER
In cmd.exe navigate to roly-united/UnityAssetStore/main/
	
	1. Edit scraper.py:
		- Scroll to the bottom and make sure the call to "scrape()" is NOT commented out
			e.g. scrape("test_repo", "email@gmail.com", "password")
			NOT  #scrape("test_repo", "email@gmail.com", "password")
		  
		- Replace the information in scrape() with your Unity Asset Store login information
		  
	2. Run the scraper from cmd.exe:
		$ python scraper.py
		
	Expected output:
		$ running scraper.py...
		$ Start scraping!
		$
		$ DevTools listening on ws://127.0.0.1:57675/devtools/browser/429d70e2-6148-4a66-b2fd-2531f0bd11be
		$ Go to 'https://assetstore.unity.com/account/assets'
		$ [0401/115845.044:INFO:CONSOLE(21943)] "Hotjar not launching due to suspicious userAgent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/100.0.4896.60 Safari/537.36", source: https://idportal-cdn-prd.unity.com/assets/application-eed523e87286a88e3339a8c22957ef746aff35569374e12ca5d132cf75ed6aa8.js (21943)
		$ Log in
		$ [0401/115847.669:INFO:CONSOLE(1)] "Refused to connect to 'https://geolocation.onetrust.com/cookieconsentpub/v1/geo/location' because it violates the following Content Security Policy directive: "connect-src 'self' tools.conversion.com *.doubleclick.net *.zdassets.com *.zendesk.com *.zopim.com https://*.zopim.com wss://unity3d.zendesk.com wss://*.zopim.com cdn.cookielaw.org privacyportal-eu.onetrust.com *.google-analytics.com *.s3.amazonaws.com *.sleeknote.com *.unity3d.com *.unitychina.cn *.cdp.internal.unity3d.com *.optimizely.com heapanalytics.com *.adroll.com *.hotjar.com ws://*.hotjar.com wss://*.hotjar.com *.resonai.com *.qualtrics.com *.kameleoon.com *.kameleoon.eu *.clarity.ms fonts.googleapis.com".
		$ ", source: https://cdn.cookielaw.org/scripttemplates/otSDKStub.js (1)
		$ [0401/115848.650:INFO:CONSOLE(3)] "Hotjar not launching due to suspicious userAgent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/100.0.4896.60 Safari/537.36", source: https://static.hotjar.com/c/hotjar-1421364.js?sv=7 (3)
		$ [0401/115848.835:INFO:CONSOLE(137)] "cfQA cookie true", source: kameleoonGlobalScript.js (137)
		$ Set page size to 50 assets
		$ [0401/115849.367:INFO:CONSOLE(1)] "console.groupEnd", source: https://sleeknotestaticcontent.sleeknote.com/c/package-core-boot.js (1)
		$ [0401/115849.418:INFO:CONSOLE(140)] "Service worker registration sw-main.js succeeded: https://assetstore.unity.com/", source: https://assetstore.unity.com/account/assets (140)
		$ Creating new repo
		$ added assets:  1
		$ added assets:  2
		$ added assets:  3
		...
		$ Finished!
	
## CHECK WHAT POPULATED INTO THE DATABASE (OPTIONAL)
In cmd.exe, navigate to roly-united/UnityAssetStore

	Create a superuser for the locally-hosted website in cmd.exe:
	$ python manage.py createsuperuser
		
	Now follow the command line prompts to create super user credentials
	
In cmd.exe, navigate to roly-united/UnityAssetStore/main

	Comment out scrape() call:
	In scraper.py, scroll to the bottom and make sure the call to "scrape()" is commented out
	
	e.g. #scrape("test_repo", "email@gmail.com", "password")
	NOT  scrape("test_repo", "email@gmail.com", "password")
			
In cmd.exe, navigate to roly-united/UnityAssetStore

	Run localhost server in cmd.exe:
	$ python manage.py runserver
		
In a browser, go to the localhost URL (by default, http://127.0.0.1:8000/)
	Go to /admin/ page (e.g. http://127.0.0.1:8000/admin/), and login using the credentials you specified before
	
From here, you can view all the assets added in "Assets" and delete any you choose. 
		  

## CREATE A DATABASE DUMP FILE:
In cmd.exe, navigate to a directory you would like to place the dump file in.
Run the below command in cmd.exe to generate a database dump file:
	
	$ pg_dump -Fc --no-acl --no-owner -h <HOST> -U <USER> -d <DB_NAME> -f uas_db.dump
	
	For our app, this is the literal command:
	$ pg_dump -Fc --no-acl --no-owner -h localhost -U lainey -d uas -f uas_db.dump 
	$ password: test
    			
## IMPORT DUMP FILE INTO HEROKU APP:
1. Create/Login to your AWS Account.
2. In the search bar saying "Search for services, features...", search for "S3" and select the result "S3"
3. Select "Create bucket"
5. Under "Bucket name" use any name you wish. Use the default selections for the other settings
6. Upload your dump file (e.g. "uas_db.dump") into the bucket you just created
7. Select the dump file in the bucket, then select "Actions" > "Share with a presigned URL"
8. In cmd.exe, navigate to your roly-united directory. Then run the below command:
	
		$ heroku pg:backups:restore --app <APP_NAME> --confirm <APP_NAME> "<GENERATED_URL>"
	
		For our app, this is the literal command:
		$ heroku pg:backups:restore --app roly-united --confirm roly-united "<GENERATED_URL>"
	
## ACCESS THE REMOTELY HOSTED APP
Go to https://roly-united.herokuapp.com/
