from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='budget_home'),
    path('see_budget/', views.check_budget, name='see_budget'),
    path('about/', views.about, name='about'),
]