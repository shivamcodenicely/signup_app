# Generated by Django 2.0.3 on 2018-03-14 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_auto_20180314_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='profile_image',
            field=models.FileField(blank=True, null=True, upload_to='img'),
        ),
    ]
