# Generated by Django 3.2.4 on 2021-07-03 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210702_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart_ids',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.cart'),
        ),
    ]