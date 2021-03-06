# Generated by Django 3.0.2 on 2020-01-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errdepo_api', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='defo', upload_to='profIcon/'),
        ),
    ]
