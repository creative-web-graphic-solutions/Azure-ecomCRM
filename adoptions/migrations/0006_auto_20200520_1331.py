# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-05-20 08:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0005_auto_20191211_1719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amazoninv',
            options={'verbose_name_plural': 'Amazoninvitems'},
        ),
        migrations.AlterField(
            model_name='payment',
            name='paymentdate',
            field=models.DateField(default=datetime.date(2020, 5, 20)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='statementperiod',
            field=models.DateField(default=datetime.date(2020, 5, 20)),
        ),
    ]
