# Generated by Django 2.0 on 2018-08-30 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.CharField(blank=True, default=None, max_length=5, null=True),
        ),
    ]
