# Generated by Django 3.0.2 on 2020-01-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20200118_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='userOrange512.png', upload_to='profile_pics', verbose_name='Profil Foto'),
        ),
    ]
