from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('unit-dp', views.index, name="index"),
    path('add-personnel/', views.addPersonnel, name="add_personnel"),
    path('personnel/<str:pk>/', views.personnel, name="personnel"),

    path('retirees/', views.retirees, name="retirees"),
    path('retiree/<str:pk>/', views.retireeView, name="retiree"),
    path('retiree/add', views.addRetiree, name="add_retiree"),
    path('delete_retiree/<str:pk>/', views.deleteRetiree, name="delete_retiree"),
]