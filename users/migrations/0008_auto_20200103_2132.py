# Generated by Django 3.0.2 on 2020-01-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200103_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tc',
            field=models.IntegerField(blank=True, null=True, verbose_name='tc'),
        ),
    ]
