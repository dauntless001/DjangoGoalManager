from django.urls import path
from . import views


app_name = 'accounts'


urlpatterns = [
    path('', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('register/', views.registerview, name='register'),
]
