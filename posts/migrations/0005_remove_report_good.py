# Generated by Django 3.1.2 on 2021-01-30 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210130_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='good',
        ),
    ]
