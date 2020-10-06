from django.shortcuts import render,redirect
from.models import Questions_and_Answers, News,Orders,Testimonials,Portfolio
from django.http import HttpResponse
import requests
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

def index(request):
	context = dict()
	q_and_a = Questions_and_Answers.objects.all()
	news = News.objects.all()[:3]
	testimonials = Testimonials.objects.filter(chek_text = True)[:5]
	portfolio = Portfolio.objects.all().filter(chek_img = True)[:6]
	context['portfolio'] = portfolio
	context['q_and_a'] = q_and_a
	context['news'] = news
	context['testimonials'] =  enumerate(testimonials, start=1) if testimonials else testimonials
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
		message = request.POST.get('comment')
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


