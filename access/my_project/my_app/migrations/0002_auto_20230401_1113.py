# Generated by Django 3.1.5 on 2023-04-01 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newemployee',
            old_name='numele',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='newemployee',
            old_name='prenumele',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='oldemployee',
            old_name='numele',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='oldemployee',
            old_name='prenumele',
            new_name='last_name',
        ),
    ]
