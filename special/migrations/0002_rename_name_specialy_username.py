# Generated by Django 4.1.6 on 2023-04-09 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('special', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialy',
            old_name='name',
            new_name='username',
        ),
    ]
