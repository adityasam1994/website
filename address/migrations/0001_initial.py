# Generated by Django 2.0 on 2018-08-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('fullname', models.CharField(max_length=100)),
                ('mobile', models.CharField(blank=True, max_length=10)),
                ('pincode', models.CharField(blank=True, max_length=30)),
                ('town', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('house', models.CharField(blank=True, max_length=100)),
                ('area', models.CharField(blank=True, max_length=50)),
                ('landmark', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]