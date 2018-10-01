# Generated by Django 2.0 on 2018-08-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20180829_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='offer',
        ),
        migrations.AddField(
            model_name='offer',
            name='products',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='offers', to='shop.Product'),
        ),
    ]
