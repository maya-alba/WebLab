# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150427_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeredservice',
            name='account',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='offeredservice',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchasedservice',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
