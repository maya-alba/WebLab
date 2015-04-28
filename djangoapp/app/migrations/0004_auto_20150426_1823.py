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
            field=models.CharField(help_text=b'Use in case that company filled', max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offeredservice',
            name='service_type',
            field=models.CharField(max_length=45, choices=[(b'LO', b'Limpieza del hogar'), (b'JA', b'Jardiner\xc3\xada'), (b'SN', b'Servicios de Ni\xc3\xb1er\xc3\xada'), (b'MA', b'Mascotas'), (b'CO', b'Comida'), (b'OT', b'Otros servicios')]),
            preserve_default=True,
        ),
    ]
