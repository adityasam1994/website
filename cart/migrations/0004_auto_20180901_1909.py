# Generated by Django 2.0 on 2018-09-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_record_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_record',
            name='product_id',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cart_record',
            name='quantity',
            field=models.IntegerField(default=1, max_length=5),
        ),
        migrations.AlterField(
            model_name='cart_record',
            name='user_id',
            field=models.IntegerField(max_length=10),
        ),
    ]
