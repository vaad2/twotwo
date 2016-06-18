import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twotwo.settings")

django.setup()

from fbask import models as fbask_models

print fbask_models.Article.objects.count()
print fbask_models.Author.objects.count()