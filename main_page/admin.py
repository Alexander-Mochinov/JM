from django.contrib import admin
from .models import Questions_and_Answers, News, Orders, Testimonials,Portfolio,Prices


@admin.register(Prices)
class PricesAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    pass

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass

@admin.register(Questions_and_Answers)
class Questions_and_AnswersAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
