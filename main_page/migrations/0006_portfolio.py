# Generated by Django 3.1 on 2020-10-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=350, verbose_name='Заголовок')),
                ('portfolio_img', models.ImageField(blank=True, upload_to='uploads/images/%Y/%m/%d/')),
                ('chek_img', models.BooleanField(default=False, verbose_name='Публиковать Фото')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
                'db_table': 'portfolio',
            },
        ),
    ]