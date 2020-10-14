from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.conf import settings

class Questions_and_Answers(models.Model):
	questions = models.CharField('Вопрос', max_length = 350)
	answers = models.TextField('Ответ')

	def __str__(self):
		return str(self.questions)
	
	class Meta:
		verbose_name  = 'Вопрос Ответ'
		verbose_name_plural = 'Вопрос Ответ'
		db_table = 'questions_and_answers'
		ordering =['questions']


class Portfolio(models.Model):
	heading = models.CharField('Заголовок',max_length = 350)
	portfolio_img = models.ImageField( upload_to='uploads/images/%Y/%m/%d/',blank=True)
	chek_img = models.BooleanField('Публиковать Фото', default=False)

	def __str__(self):
		return str(self.heading)
	
	class Meta:
		verbose_name  = 'Портфолио'
		verbose_name_plural = 'Портфолио'
		db_table = 'portfolio'

class Prices(models.Model):
	heading = models.CharField('Заголовок',max_length = 350)
	coast = models.PositiveIntegerField('Стоимость')
	pakeges = models.TextField('Пакет услуг')

	def __str__(self):
		return str(self.heading)
	
	class Meta:
		verbose_name  = 'Цена'
		verbose_name_plural = 'Цены'
		db_table = 'prices'


class News(models.Model):
	heading = models.CharField('Заголовок',max_length = 350)
	# Фото проекта 
	project_img_one = models.ImageField( upload_to='uploads/images/%Y/%m/%d/',blank=True)
	
	heading_for_img_one =  models.CharField('Заголовок к первой фотографии',max_length = 350,blank=True,null=True)

	post_for_img_one =  models.CharField('Описание к первой фотографии',max_length = 350,blank=True,null=True)

	# Фото проекта 
	project_img_two = models.ImageField( upload_to='uploads/images/%Y/%m/%d/',blank=True)
	
	heading_for_img_two =  models.CharField('Заголовок ко второй фотографии',max_length = 350,blank=True,null=True)
	
	post_for_img_two =  models.CharField('Описание ко второй фотографии',max_length = 350,blank=True,null=True)

	# Фото проекта 
	project_img_three = models.ImageField( upload_to='uploads/images/%Y/%m/%d/',blank=True)

	heading_for_img_three =  models.CharField('Заголовок к третьей фотографии',max_length = 350,blank=True,null=True)

	post_for_img_three =  models.CharField('Описание к третьей фотографии',max_length = 350,blank=True,null=True)

	publication_date = models.DateField("Дата публикации", default=date.today, db_index=True)

	price = models.ForeignKey(Prices, on_delete=models.SET_NULL,null=True, verbose_name="Цена на ивент)")
	# Пост
	post = models.TextField('Анонс')


	def __str__(self):
		return str(self.heading)

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])
	
	class Meta:
		verbose_name  = 'Анонс'
		verbose_name_plural = 'Анонсы'
		db_table = 'news'
		ordering =['publication_date']


class Orders(models.Model):
	name = models.CharField('Имя заказчика', max_length=250)
	email = models.EmailField('Эл. почта')
	message = models.TextField('Сообщение от пользователя')
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format.")
	phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
	publication_date = models.DateField("Дата публикации", default=date.today, db_index=True)
	news = models.ForeignKey(News, verbose_name = 'Заказ на тему', on_delete=models.CASCADE)

	def __str__(self):
		return str(self.news) + ' : ' + str(self.name)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		subject = 'Заказ на съёмку'
		message = 'Получен новый заказ на съёмку {}, от {} \nКонтактные данные:  тел. {}, почта: {}\nСообщение: {}'.format(self.news, self.name, self.phone,self.email, self.message)
		send_mail(subject,message,from_email,to_email,fail_silently=False,)

	class Meta:
		verbose_name  = 'Заказ'
		verbose_name_plural = 'Заказы'
		db_table = 'orders'
		ordering =['publication_date']


class Testimonials(models.Model):
	name = models.CharField('Имя комментатора', max_length=250)
	email = models.EmailField('Эл. почта')
	message = models.TextField('Сообщение от пользователя')
	publication_date = models.DateField("Дата публикации", default=date.today, db_index=True)
	chek_text = models.BooleanField('Публиковать комментарий', default=False)

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name  = 'Отзыв'
		verbose_name_plural = 'Отзывы'
		db_table = 'testimonials'
		ordering =['publication_date']