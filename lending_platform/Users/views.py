from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from lending.models import Loan, LoanRequest

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            # Create a new user
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')  # Redirect to login after registration
        else:
            return HttpResponse('All fields are required.') 

    return render(request, 'Users/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            return render(request, 'Users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'Users/login.html')


def logout_view(request):
    logout(request)  # Logs the user out
    return redirect('login') 




