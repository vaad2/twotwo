# -*- coding: utf-8 -*-
import os
import random
import shutil
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twotwo.settings")


django.setup()

from django_dynamic_fixture import G
from django.core.management import call_command
from django.contrib.auth.models import User
from django.conf import settings

from fbask import models as fbask_models
from faker import Factory


def init(is_reset=True, is_dir_clean=True):
    if is_reset:
        call_command('reset_db', interactive=0)

    if is_dir_clean:
        for dir2clean in ['cache', 'infoimage', 'fact', 'news']:
            dir2clean = os.path.join(settings.BASE_DIR, 'media', dir2clean)
            if os.path.exists(dir2clean):
                shutil.rmtree(dir2clean)

    call_command('makemigrations')
    call_command('migrate')

    admin = G(User, username='admin', is_active=True, is_staff=True,
              is_superuser=True)
    admin.set_password('hello')
    admin.save()

    fake = Factory.create()
    for i in xrange(20):
        G(fbask_models.Author,
          first_name=fake.first_name(),
          last_name=fake.last_name())
        G(fbask_models.Article,
          title=fake.company(),
          content=fake.address())

if __name__ == '__main__':
    init()
