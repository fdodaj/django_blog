# Generated by Django 3.1.2 on 2021-01-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210113_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
