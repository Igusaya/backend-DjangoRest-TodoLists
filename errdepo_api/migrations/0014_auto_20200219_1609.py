# Generated by Django 3.0.2 on 2020-02-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errdepo_api', '0013_auto_20200219_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]