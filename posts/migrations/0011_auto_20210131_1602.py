# Generated by Django 3.1.2 on 2021-01-31 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20210131_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='name',
            new_name='author',
        ),
    ]