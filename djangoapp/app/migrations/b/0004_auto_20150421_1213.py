# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150420_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeredservice',
            name='company_name',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
    ]
