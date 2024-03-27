"""
URL configuration for ZomatoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from registration_app import views as rviews
from payement_app import views as pviews
from order_app import views as oview

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', rviews.homepage),
    path('home/', rviews.homepage,name='home'),
    path('register/',rviews.user_registration,name='register'),
    path('login/',rviews.user_login,name='login'),
    path('userdata/',rviews.user_details,name='userdata'),

    path('index/',pviews.index_page),

    path('order/',oview.index_page_order)


]





