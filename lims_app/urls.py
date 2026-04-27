"""
URL configuration for lims_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('readers/', views.readers_tab, name='readers_tab'),
    path('save', views.save_student),
    path('readers/add', views.save_reader),
    path('books/', views.book_list, name='book_list'),
    path('books/add', views.save_book),
    path('readers/delete/<int:reader_id>/', views.delete_reader, name='delete_reader'),
    path('books/delete/<int:id>/', views.delete_book, name='delete_book'),
    path('collection/', views.borrowing_list_add, name='borrowing_list_add'),
    path('borrowings/delete/<int:borrowing_id>/', views.delete_borrower, name='delete_borrower'),
]

