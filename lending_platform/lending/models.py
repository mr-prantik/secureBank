from django.db import models
from django.contrib.auth.models import User

class Lender(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    available_balance = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username


class Borrower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_score = models.IntegerField()
    requested_loan_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username



class LoanRequest(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loan_requests')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=10, default='pending')  # pending, approved, rejected
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.borrower.username} - {self.amount} at {self.interest_rate}% interest'

class Loan(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_loans')
    lender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lent_loans')
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_start_date = models.DateField()
    loan_end_date = models.DateField()

    def __str__(self):
        return f'Loan: {self.borrower.username} borrows {self.loan_amount} from {self.lender.username}'



