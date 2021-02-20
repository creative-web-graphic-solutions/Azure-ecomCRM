# Generated by Django 2.2.7 on 2019-12-09 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0003_auto_20191207_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='paid', max_length=250),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paymentdate',
            field=models.DateField(default=datetime.date(2019, 12, 9)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='statementperiod',
            field=models.DateField(default=datetime.date(2019, 12, 9)),
        ),
    ]