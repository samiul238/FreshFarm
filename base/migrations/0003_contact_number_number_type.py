# Generated by Django 3.2.4 on 2021-06-30 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_number',
            name='number_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]