from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('menuitem/', views.MenuItemsView.as_view()),
    path('menuitem/<int:pk>/', views.SingleMenuItemView.as_view()),

]
