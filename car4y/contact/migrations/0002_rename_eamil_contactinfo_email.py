# Generated by Django 4.1.7 on 2023-02-27 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinfo',
            old_name='eamil',
            new_name='email',
        ),
    ]
