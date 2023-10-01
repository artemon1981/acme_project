# Generated by Django 3.2.16 on 2023-09-28 20:19

import birthday.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, help_text='Необязательное поле', max_length=20, verbose_name='Фамилия')),
                ('birthday', models.DateField(validators=[birthday.validators.real_age], verbose_name='Дата рождения')),
                ('image', models.ImageField(blank=True, upload_to='birthdays_images', verbose_name='Фото')),
            ],
        ),
        migrations.AddConstraint(
            model_name='birthday',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'birthday'), name='Unique person constraint'),
        ),
    ]
