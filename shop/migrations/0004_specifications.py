# Generated by Django 2.1 on 2018-08-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180816_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('spec1_name', models.CharField(max_length=50)),
                ('spec1_value', models.CharField(max_length=100)),
            ],
        ),
    ]
