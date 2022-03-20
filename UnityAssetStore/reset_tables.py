import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'UAS.settings'
django.setup()

from main.models import *

Repo.objects.all().delete()
Asset.objects.all().delete()
Label.objects.all().delete()
Category.objects.all().delete()