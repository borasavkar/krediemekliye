# Generated by Django 3.0.2 on 2020-01-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200103_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('İstanbul', 'İstanbul'), ('Ankara', 'Ankara'), ('İzmir', 'İzmir'), ('Diğer', 'Diğer')], default='', max_length=20, verbose_name='Şehir'),
        ),
    ]
