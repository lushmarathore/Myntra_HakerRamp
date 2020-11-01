"""dlw_integrate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from dlw.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('online_rental/',online_rental,name='online_rental'),
    path('make_update/',make_update,name='make_update'),
    path('delete_dress1/',delete_dress1,name='delete_dress1'),
    
    path('login_page_shed1/',login_page_shed1,name='login_page_shed1'),
    path('display/',display,name='display'),
    path('registration/',registration,name='registration'),
    path('upcoming/',upcoming,name='upcoming'),
    path('logout_page_shed/',logout_page_shed,name='logout_page_shed'),
    path('login_page_shed/',login_page_shed,name='login_page_shed'),
    path('shed_dashboard/<type1>',shed_dashboard,name='shed_dashboard'),
    path('shed_dashboard/',shed_dashboard,name='shed_dashboard'),


    path('',login_cust,name="loginpage_cust"),
    path('welcome',showdetail,name="items"),
    path('showitemdetail/<itemid>/<userid>',showdetail,name="showitemdetail"),
    path('rental_register',rental_register,name="rental_register"),
    path('loginpage_cust',login_cust,name="loginpage_cust"),
    path('booking/<itemid>',booking,name="booking"),
    path('ajax/check_avail_booking',check_avail_booking,name='check_avail_booking'),	
    path('history_cust/<userid>',history_cust,name='history_cust'),
    path('history_cust',history_cust,name='history_cust'),
    path('view_transactions',view_transactions,name='view_trans'),
    path('ajax/admin_bydate',admin_bydate,name='admin_bydate'),	
    path('items',admin_item,name='items_admin'),
    path('view_cust',view_cust,name='view_cust'),
    path('ajax/admin_byusername',admin_byusername,name='admin_byusername'),	
    path('info',view_info,name='view_info'),
    path('feedback',feedback,name='feedback'),
    
    

]









if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)