# Generated by Django 3.1 on 2020-10-06 18:20

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_auto_20201005_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя заказчика')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл. почта')),
                ('message', models.TextField(verbose_name='Сообщение от пользователя')),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format.', regex='^\\+?1?\\d{9,15}$')])),
                ('publication_date', models.DateField(db_index=True, default=datetime.date.today, verbose_name='Дата публикации')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.news', verbose_name='Заказ на тему')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'orders',
                'ordering': ['publication_date'],
            },
        ),
    ]
