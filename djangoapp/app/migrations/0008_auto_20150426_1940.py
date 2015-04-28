# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150426_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeredservice',
            name='service_image',
            field=models.ImageField(upload_to=b'C:\\xampp\\htdocs\\djangoProject\\djangoapp/media/offeredservice', blank=True),
        ),
    ]
