# Generated by Django 3.2.4 on 2021-07-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_replyreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag_list',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]