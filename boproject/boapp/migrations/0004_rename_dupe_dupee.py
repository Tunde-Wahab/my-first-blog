# Generated by Django 3.2.14 on 2022-08-10 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boapp', '0003_rename_dip_dupe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dupe',
            new_name='Dupee',
        ),
    ]
