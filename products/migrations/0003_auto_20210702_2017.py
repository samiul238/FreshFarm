# Generated by Django 3.2.4 on 2021-07-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_order_delivery_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
