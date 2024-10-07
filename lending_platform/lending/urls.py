from django.urls import path
from .views import request_loan
urlpatterns = [
    path('request/', request_loan, name='request-loan'),
    
]
