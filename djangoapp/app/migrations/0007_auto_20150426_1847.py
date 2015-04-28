# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150426_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeredservice',
            name='account',
            field=models.BigIntegerField(max_length=16),
        ),
    ]
