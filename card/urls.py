from django.urls import path
from . import views



app_name = 'card'

urlpatterns = [
    path('', views.card, name='card'),
    path('<int:id>/', views.detail, name='card_detail'),
]