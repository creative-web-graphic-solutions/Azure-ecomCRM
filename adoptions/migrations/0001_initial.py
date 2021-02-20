# Generated by Django 2.2.7 on 2019-12-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amazoninv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.IntegerField()),
                ('Description', models.CharField(max_length=300)),
                ('BanggoodID', models.IntegerField()),
                ('Website', models.CharField(max_length=250)),
                ('StockInfo', models.CharField(max_length=200)),
                ('Qty', models.IntegerField()),
                ('Cost', models.IntegerField()),
                ('promotion_enddate', models.DateTimeField(blank=True, null=True)),
                ('reorder', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoicetracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoicenumber', models.IntegerField()),
                ('invoicedate', models.DateTimeField()),
                ('BillAmount', models.IntegerField()),
                ('TotalPaid', models.IntegerField()),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentnumber', models.IntegerField()),
                ('paymentdate', models.DateTimeField()),
                ('paymentamount', models.IntegerField()),
                ('paymentmethod', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=250)),
                ('Paynote', models.CharField(max_length=250)),
            ],
        ),
    ]