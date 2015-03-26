# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OfferedService',
            fields=[
                ('seviceID', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=45)),
                ('service_type', models.CharField(max_length=45)),
                ('account', models.BigIntegerField()),
                ('company', models.BooleanField()),
                ('company_name', models.CharField(max_length=45)),
                ('price', models.DecimalField(max_digits=7, decimal_places=2)),
                ('price_delimiter', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('service_image', models.IntegerField()),
                ('brief_description', models.CharField(max_length=140)),
                ('descripton', models.TextField()),
                ('service_email', models.EmailField(max_length=70)),
                ('telephone', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PurchasedService',
            fields=[
                ('purchased_service_id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('total', models.DecimalField(max_digits=7, decimal_places=2)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Comprado'), (1, b'Enviado'), (2, b'Entregado'), (3, b'Cerrado')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=70, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=30, verbose_name=b'Primer nombre')),
                ('lastName', models.CharField(max_length=30, verbose_name=b'Apellido del usuario')),
                ('rating', models.IntegerField(null=True, blank=True)),
                ('profileImage', models.ImageField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='purchasedservice',
            name='client_email',
            field=models.ForeignKey(to='app.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchasedservice',
            name='seller_email',
            field=models.ForeignKey(to='app.OfferedService'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offeredservice',
            name='user_email',
            field=models.ForeignKey(to='app.User'),
            preserve_default=True,
        ),
    ]
