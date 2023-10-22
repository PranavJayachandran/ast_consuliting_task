from django.urls import path

from . import views

urlpatterns = [path('',views.index,name='index'),
               path('delete/<str:dynamic_id>/', views.delete, name='delete'),
               path('edit/<str:edit_id>/', views.edit, name='edit'),
               path('update/', views.update, name='update')]