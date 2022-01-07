# Generated by Django 3.2.9 on 2021-12-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('male', 'Мужской пол'), ('female', 'Женский пол')], default='', max_length=100, verbose_name='Пол пользователя'),
        ),
    ]