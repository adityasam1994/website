# Generated by Django 2.1 on 2018-08-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_specifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='specifications',
            name='spec2_name',
            field=models.CharField(default='spec', max_length=50),
        ),
        migrations.AddField(
            model_name='specifications',
            name='spec2_value',
            field=models.CharField(default='spec', max_length=100),
        ),
        migrations.AddField(
            model_name='specifications',
            name='spec3_name',
            field=models.CharField(default='spec', max_length=50),
        ),
        migrations.AddField(
            model_name='specifications',
            name='spec3_value',
            field=models.CharField(default='spec', max_length=100),
        ),
        migrations.AddField(
            model_name='specifications',
            name='spec4_name',
            field=models.CharField(default='spec', max_length=50),
        ),
        migrations.AddField(
            model_name='specifications',
            name='spec4_value',
            field=models.CharField(default='spec', max_length=100),
        ),
        migrations.AddField(
            model_name='specifications',
            name='spec5_name',
            field=models.CharField(default='spec', max_length=50),
        ),
        migrations.AddField(
            model_name='specifications',
            name='spec5_value',
            field=models.CharField(default='spec', max_length=100),
        ),
        migrations.AddField(
            model_name='specifications',
            name='spec6_name',
            field=models.CharField(default='spec', max_length=50),
        ),
        migrations.AddField(
            model_name='specifications',
            name='spec6_value',
            field=models.CharField(default='spec', max_length=100),
        ),
        migrations.AlterField(
            model_name='specifications',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
        migrations.AlterField(
            model_name='specifications',
            name='spec1_name',
            field=models.CharField(default='spec', max_length=50),
        ),
        migrations.AlterField(
            model_name='specifications',
            name='spec1_value',
            field=models.CharField(default='spec', max_length=100),
        ),
    ]
