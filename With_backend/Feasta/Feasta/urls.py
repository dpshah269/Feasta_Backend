"""Feasta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import login.views as lv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name = "admin"),
    path('register/', lv.Register, name="register"),
    path('login/', lv.Login, name="login"),
    path('', lv.Home, name="home"),
    path('about/', lv.About, name="about"),
    path('blog/', lv.Blog, name="blog"),
    path('blog-details/', lv.BlogDetails, name="blog-details"),
    path('contact/', lv.Contact, name="contact"),
    path('cart/', lv.Cart, name="cart"),
    path('admin-menu/',lv.index, name="Admin-Menu"),
    path('menu/',lv.menu, name="menu"),
    path('add-item/',lv.Add_Item, name="Add-Item"),
    path('dashboard/',lv.Admin_Index, name="Admin-Index"),
    path('add-category/',lv.Add_Category, name="Add-Category")
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)