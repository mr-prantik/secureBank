"""
URL configuration for lending_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from lending.views import home_view
from lending import views as lending_views
from lending import views
from Users import views

urlpatterns = [
    path('', lending_views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),  # Logout URL
    path('dashboard/', lending_views.dashboard_view, name='dashboard'),  # Dashboard URL
    path('request/', lending_views.request_loan, name='request'),
    path('borrow/', lending_views.create_loan_request, name='borrow'),
    path('lend/<int:loan_request_id>/', lending_views.lend_money, name='lend'),
    path('lending/', lending_views.home_view, name='lending'),
]
