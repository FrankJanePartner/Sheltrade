from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid

# Create your models here.
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userBalance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50)
    transaction_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"



# class Deposit(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deposit')
#     proofOfPayment = models.ImageField(upload_to='proofs/')
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     timestamp = models.DateTimeField(default=datetime.now)

#     def __str__(self):
#         return f"Deposited {self.pk} - User {self.user.username}"


# class Withdrawal(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='withdrawal')
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     timestamp = models.DateTimeField(default=datetime.now)

#     def approve(self):
#         self.status = 'approved'
#         self.save()

#     def __str__(self):
#         return f"Withdrawal by {self.user.username} - {self.amount}"

