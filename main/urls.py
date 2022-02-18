from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path ('',views.home_page,name='home_page'),
    path ('result',views.result_page,name='result_page'),
]
