# UnityAssetStore
A project through CSE 5915 at The Ohio State University.

Important to remember to turn off debug in settings.py once site is in production, that shouldn't be for a while.

HOW TO RUN:
 - Navigate to the directory that holds the manage.py file, should be within the last of the UnityAssetStore nested folders.
 - Run the command 'python3 manage.py runserver'. Could be just python instead of python3 if that's what version of python you have installed (not sure)
 - Terminal should provide a link that looks like an IP address where the webpage is being hosted.

HOW TO NAVIGATE:
 - Home Page: '/home' Path
 - Join Page: '/join' Path
 - Create Page: '/create' Path
 - Asset Info Page: '/asset_info' Path
 - Edit Info Page: '/edit_info' Path
 - Add Asset Page: '/add_asset' Path
 - Credits Page: '/credits' Path


HOW TO MAKE MIGRATION FILES:
 - Once changes are made to database, navigate to the directory with the manage.py file
 - run "python manage.py makemigrations" (this effectively stages the migrations before committing them)
 - run "python manage.py migrate" (this effectively commits the changes and generates a new migration file)

 Requirements 
 - gunicorn
 - django-heroku