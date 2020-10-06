# Generated by Django 3.1 on 2020-10-06 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя комментатора')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл. почта')),
                ('message', models.TextField(verbose_name='Сообщение от пользователя')),
                ('publication_date', models.DateField(db_index=True, default=datetime.date.today, verbose_name='Дата публикации')),
                ('chek_text', models.BooleanField(default=False, verbose_name='Публиковать комментарий')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'db_table': 'testimonials',
                'ordering': ['publication_date'],
            },
        ),
    ]