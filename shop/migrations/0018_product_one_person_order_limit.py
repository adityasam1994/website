# Generated by Django 2.0 on 2018-09-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_remove_offer_activate'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='one_person_order_limit',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
