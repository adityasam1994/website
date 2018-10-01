# Generated by Django 2.1 on 2018-08-24 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180816_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Front_Page_Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
            options={
                'verbose_name': 'Front_Page_Section',
                'verbose_name_plural': 'Front_Page_Sections',
            },
        ),
        migrations.CreateModel(
            name='Highlights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight1_name', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('highlight1_image', models.ImageField(blank=True, default=None, null=True, upload_to='highlights/%Y/%m/%d')),
                ('highlight2_name', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('highlight2_image', models.ImageField(blank=True, default=None, null=True, upload_to='highlights/%Y/%m/%d')),
                ('highlight3_name', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('highlight3_image', models.ImageField(blank=True, default=None, null=True, upload_to='highlights/%Y/%m/%d')),
                ('highlight4_name', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('highlight4_image', models.ImageField(blank=True, default=None, null=True, upload_to='highlights/%Y/%m/%d')),
                ('highlight5_name', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('highlight5_image', models.ImageField(blank=True, default=None, null=True, upload_to='highlights/%Y/%m/%d')),
                ('highlight6_name', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('highlight6_image', models.ImageField(blank=True, default=None, null=True, upload_to='highlights/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'highlight',
                'verbose_name_plural': 'highlights',
                'ordering': ('product',),
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='highlights',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='offer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Offer'),
        ),
    ]
