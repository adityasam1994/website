# Generated by Django 2.0 on 2018-09-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20180904_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='charge_id',
            field=models.CharField(blank=True, default=False, max_length=200, null=True),
        ),
    ]
