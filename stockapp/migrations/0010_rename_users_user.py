# Generated by Django 3.2.5 on 2021-08-19 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0009_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]