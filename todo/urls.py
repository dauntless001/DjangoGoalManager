from django.urls import path
from . import views

app_name='todo'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add-todo/', views.create_view, name='create'),
    path('<str:slug>/delete/', views.delete_view, name='delete'),
    path('<str:slug>/complete/', views.complete_view, name='complete'),
    path('<str:slug>/edit/', views.edit_view, name='edit'),
]
