# Generated by Django 3.0.2 on 2020-01-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200103_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ad',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='soyad',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tel',
            field=models.IntegerField(blank=True, null=True, verbose_name='tel'),
        ),
    ]
