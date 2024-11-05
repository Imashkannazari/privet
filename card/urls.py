from django.urls import path
from . import views



app_name = 'card'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.card, name='card'),
    path('projects/<slug:slug>/', views.detail, name='card_detail'),
    path('programmers/', views.programmers, name='programmers'),
]