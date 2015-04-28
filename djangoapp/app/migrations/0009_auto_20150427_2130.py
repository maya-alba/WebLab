# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20150426_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offeredservice',
            old_name='descripton',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='offeredservice',
            old_name='seviceID',
            new_name='serviceID',
        ),
        migrations.AlterField(
            model_name='offeredservice',
            name='service_image',
            field=models.ImageField(upload_to=b'C:\\xampp\\htdocs\\djangoProject\\djangoapp/media/offered_service', blank=True),
        ),
    ]
