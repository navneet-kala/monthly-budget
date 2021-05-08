from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('expenses/', views.expenses, name='expenses'),
    path('categories/', views.categories, name='categories'),
]
