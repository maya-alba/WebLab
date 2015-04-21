# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150420_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='rating',
        ),
        migrations.AddField(
            model_name='offeredservice',
            name='rating',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchasedservice',
            name='rating',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
