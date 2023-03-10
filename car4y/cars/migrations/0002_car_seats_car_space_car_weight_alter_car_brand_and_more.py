# Generated by Django 4.1.7 on 2023-02-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='car',
            name='space',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='car',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
