from django.urls import path
from . import views

urlpatterns = [
	path('', views.index , name = 'index'),
	path('post/<int:id>/', views.post_detail, name='post_detail'),
	path('create-order/<int:id_news>/', views.create_order, name='create_order'),
	path('add_testimonial/', views.add_testimonial, name="add_testimonial"),
	path('questions/', views.questions, name='questions'),
	path('order/<int:id>/', views.order, name="order"),
]
