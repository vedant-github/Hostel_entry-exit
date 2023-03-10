"""hostelentryexit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hostels/', views.hostel_list),
    path('hostels/<str:username>', views.hostel_detail),
    path('database/', views.database_list),
    path('database/<int:id>', views.database_detail),
    path('users/', views.users_list),
    path('users/<str:roll_no>', views.users_detail),
    path('tempdata/', views.tempdata_list),
    path('tempdata/<str:rollnum_1>', views.tempdata_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)   