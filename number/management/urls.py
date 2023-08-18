from django.urls import path
from . import views

urlpatterns = [
    path('number/', views.fetch_nums, name='fetch_nums')
]