from django.shortcuts import render,redirect
from.models import Questions_and_Answers, News,Orders,Testimonials,Portfolio,Testimonials,Prices
from django.http import HttpResponse, HttpResponseRedirect
import requests
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

def order(request, id):
	price = Prices.objects.get(id = id)
	if request.method == 'POST':
		name = request.POST.get('name','')
		email = request.POST.get('email', '')
		message = request.POST.get('comment', '')
		phone = request.POST.get('phone', '')
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		subject = 'Сообщение от пользователя'
		message = '{} \nКонтактные данные: \nПочта: {}\nКонтактный номер телефона: {} \nСообщение: {}\nЦеновой тип : {}'.format(name, email, phone,message,price)
		send_mail(subject,message,from_email,to_email,fail_silently=False,)	
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	
def index(request):
	context = dict()
	q_and_a = Questions_and_Answers.objects.all()
	news = News.objects.all()[:3]
	testimonials = Testimonials.objects.filter(chek_text = True)[:5]
	portfolio = Portfolio.objects.all().filter(chek_img = True)[:6]
	prices = Prices.objects.all()[:4]
	context['portfolio'] = portfolio
	context['q_and_a'] = q_and_a
	context['news'] = news
	context['testimonials'] =  enumerate(testimonials, start=1) if testimonials else testimonials
	context['prices'] = prices
	return render(request, 'index.html', context)

def post_detail(request, id):
	
	context = dict()
	news = News.objects.get(id = id)
	context['news'] = news
	return render(request, 'detail/post_detail.html', context)

def create_order(request, id_news):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('comment', 'Пусто')
		phone = request.POST.get('phone')
		Orders.objects.create(
			name = name,
			email = email,
			message = message,
			phone = phone,
			news_id = id_news,
		)
		return redirect('/post/'+ str(id_news) + '/')
	else:
		return redirect('/post/'+ str(id_news) + '/')

def questions(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('comment')
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		subject = 'Сообщение от пользователя'
		message = '{} \nКонтактные данные: \nпочта: {}\nСообщение: {}'.format(name, email, message)
		send_mail(subject,message,from_email,to_email,fail_silently=False,)		
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def add_testimonial(request):
	if request.method == "GET":
		name = request.GET.get('name')
			
		email = request.GET.get('email')
		text = request.GET.get('text')
		if len(name) and len(email) < 10:
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
		Testimonials.objects.create(
			name = name,
			email = email,
			message = text,
		)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
