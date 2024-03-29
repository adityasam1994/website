# Generated by Django 2.1 on 2018-08-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180817_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='area',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='house',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='landmark',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='town',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
