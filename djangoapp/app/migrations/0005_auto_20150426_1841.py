# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150426_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeredservice',
            name='account',
            field=models.IntegerField(max_length=16),
        ),
        migrations.AlterField(
            model_name='offeredservice',
            name='city',
            field=models.CharField(max_length=45, choices=[(b'ZAP', b'Zapopan'), (b'TON', b'Tonala'), (b'GDL', b'Guadalajara')]),
        ),
        migrations.AlterField(
            model_name='offeredservice',
            name='price_delimiter',
            field=models.CharField(max_length=45, choices=[(b'D', b'D\xc3\xada'), (b'H', b'Hora'), (b'U', b'Unidad'), (b'S', b'Servicio')]),
        ),
        migrations.AlterField(
            model_name='offeredservice',
            name='state',
            field=models.CharField(max_length=45, choices=[(b'JAL', b'Jalisco')]),
        ),
    ]
