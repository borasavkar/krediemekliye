# Generated by Django 3.0.3 on 2020-02-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20200207_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tc',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Tc'),
        ),
    ]
