from django.shortcuts import render
from .utils import generate_narration
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Transaction, Wallet, DepositNarations, WithdrawalAccount, Withdrawal
from django.contrib.auth.models import User
from decimal import Decimal
from django.shortcuts import redirect


# Create your views here.
@login_required
def wallet(request):
    user = request.user

    wallet = Wallet.objects.get(user=user)
    transactions = Transaction.objects.filter(user=user)
    return render(request, 'wallet/wallet.html', {"wallet":wallet, "transactions":transactions})


@login_required
def deposit(request):
    narration = generate_narration()
    
    return render(request, 'wallet/deposite.html', {'narration': narration})

@login_required
def deposit_submit_view(request):
    if request.method == 'POST':
        narration = request.POST.get('narration')

        amount = Decimal(request.POST.get('amount') or 0)
        proof_of_payment = request.FILES.get('proof_of_payment')
        

        transaction = Transaction(user=request.user, transaction_type='Deposit', proof_of_payment=proof_of_payment, amount=amount, status="pending")
        transaction.save()
        deposit_naration = DepositNarations(user=request.user, narration=narration, transaction_id=transaction)
        deposit_naration.save()

        messages.info(request, 'Deposit sent! Awaiting approval.')
        return redirect('wallet:wallet')
        # Handle the deposit logic here using the narration

@login_required
def withdrawal(request):
    withdrawalAccounts = WithdrawalAccount.objects.filter(user=request.user)
    
    return render(request, 'wallet/withdraw.html', {"withdrawalAccounts":withdrawalAccounts})


@login_required
def withdrawal_submit_view(request):
    if request.method == 'POST':
        selected_account_id = request.POST.get('SelectedAcount')
        amount = Decimal(request.POST.get('amount'))
        withdrawal_account= WithdrawalAccount.objects.get(id=selected_account_id, user=request.user)
        wallet = Wallet.objects.get(user=request.user)

        if wallet.userBalance >= amount:
            transaction = Transaction(user=request.user, transaction_type='Withdrawal', amount=amount, status="pending")
            transaction.save()
            withdrawal = Withdrawal(user=request.user, transaction_id=transaction, acount_name=withdrawal_account.account_name, acount_number=withdrawal_account.account_number, BankName=withdrawal_account.bank_name)
            withdrawal.save()

            messages.success(request, f"Withdrawal processed from {withdrawal_account.account_name}.")
            return redirect('wallet:wallet')
            
        else:
            messages.info(request, 'Insufficient balance.')
        return redirect('wallet:withdraw')


@login_required
def AddAccount(request):
    if request.method == 'POST':
        accountName = request.POST.get('accountName')
        bankName = request.POST.get('bankName')
        accountNumber = request.POST.get('accountNumber')

        address = WithdrawalAccount(user=request.user, account_name=accountName, account_number=accountNumber, bank_name=bankName)
        address.save()
        messages.info(request, 'Account added sucessfully.')
        return redirect('wallet:wallet')
    else:
        return render(request, 'wallet/AddWithdrawalAccount.html')
    


    