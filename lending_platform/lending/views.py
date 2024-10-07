from django.shortcuts import render
from .forms import LoanRequestForm
from .models import Loan
from django.contrib.auth.decorators import login_required
from .models import Loan, LoanRequest
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

def home_view(request):
    return render(request, 'lending/home.html')


def request_loan(request):
    if request.method == 'POST':
        form = LoanRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loan-list')
    else:
        form = LoanRequestForm()
    return render(request, 'lending/loan_request.html', {'form': form})

@login_required
def dashboard_view(request):
    pending_loan_requests = LoanRequest.objects.filter(status='pending')

    context = {
        'pending_loan_requests': pending_loan_requests,
    }
    return render(request, 'lending/dashboard.html', context)

@login_required
def create_loan_request(request):
    if request.method == 'POST':
        form = LoanRequestForm(request.POST)
        if form.is_valid():
            loan_request = form.save(commit=False)
            loan_request.borrower = request.user
            loan_request.save()
            return redirect('dashboard')  
    else:
        form = LoanRequestForm()

    context = {'form': form}
    return render(request, 'lending/create_loan_request.html', context)

@login_required
def lend_money(request, loan_request_id):
    loan_request = LoanRequest.objects.get(id=loan_request_id, status='pending')

    if request.method == 'POST':
        # Fulfill the loan request
        Loan.objects.create(
            borrower=loan_request.borrower,
            lender=request.user,  # The current logged-in user is the lender
            loan_amount=loan_request.amount,
            interest_rate=loan_request.interest_rate,
            loan_start_date=timezone.now(),
            loan_end_date=timezone.now() + timedelta(days=365)  # 1-year loan period for simplicity
        )
        # Update the loan request status to 'approved'
        loan_request.status = 'approved'
        loan_request.save()
        return redirect('dashboard')

    context = {'loan_request': loan_request}
    return render(request, 'lending/lend_money.html', context)


