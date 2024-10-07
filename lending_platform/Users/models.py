from django.db import models
from django.contrib.auth.models import User

class LoanRequest(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Added amount field
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Optional default for interest_rate
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'), 
        ('approved', 'Approved'), 
        ('rejected', 'Rejected')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.borrower.username} - {self.amount} - {self.interest_rate}%"

class Loan(models.Model):
    lender = models.ForeignKey(User, related_name='loan_lender', on_delete=models.CASCADE)  # Unique related_name
    borrower = models.ForeignKey(User, related_name='loan_borrower', on_delete=models.CASCADE)  # Unique related_name
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_start_date = models.DateTimeField(auto_now_add=True)
    loan_end_date = models.DateTimeField()
    
    def __str__(self):
        return f"Loan from {self.lender.username} to {self.borrower.username} for {self.loan_amount}"
