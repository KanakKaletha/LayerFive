"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    
    
    path('room_count_by_category/', views.room_count_by_category, name='room_count_by_category'),
    path('room_count_by_category/<str:date>/', views.room_count_by_category, name='room_count_by_category'),
    path('room_count_by_category_submit/', views.room_count_by_category_submit, name='room_count_by_category_submit'),
    
    path('room_count_by_category_range/', views.room_count_by_category_range, name='room_count_by_category_range'),
    path('room_count_by_category_range/<str:start_date>/<str:end_date>/<str:category>/', views.room_count_by_category_range, name='room_count_by_category_range'),
    path('room_count_by_category_range_submit/', views.room_count_by_category_range_submit, name='room_count_by_category_range_submit'),
    
    path('guest_details/', views.guest_details, name='guest_details'),
    path('guest_details/<int:room_id>/', views.guest_details, name='guest_details'),
    path('guest_details_submit/', views.guest_details_submit, name='guest_details_submit'),
    
]
