from django.urls import path
from . import views
from . import objectives_view
app_name = 'goal'


urlpatterns = [
    path('goals-list/', views.goal_list, name='list'),
    path('set-goals/', views.goal_create, name='create'),
    path('<str:slug>/', views.goal_detail, name='detail'),
    path('<str:slug>/delete/', views.goal_delete, name='delete'),
    path('<str:slug>/complete/', views.goal_complete, name='complete'),
    path('<str:slug>/edit/', views.goal_edit, name='edit'),
    path('<str:slug>/<int:id>/delete/', objectives_view.obj_delete, name='obj_delete'),
    path('<str:slug>/<int:id>/complete/', objectives_view.obj_complete, name='obj_complete'),
   

]
