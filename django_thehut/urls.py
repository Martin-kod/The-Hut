"""django_thehut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from thehut.views import get_homepage, book_table, edit_booking, delete_booking

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_homepage, name='home'),
    path('thehut_booking', book_table, name='book_table'),
    path('edit/<booking_id>', edit_booking, name='edit'),
    path('delete/<booking_id>', delete_booking, name='delete')
]
