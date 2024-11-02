from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from wallet.models import Transaction, Wallet
from giftcard.models import GiftCard

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def aboutus(request):
    return render(request, 'core/aboutus.html')

@login_required
def dashboard(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user)
    giftcards = GiftCard.objects.filter(seller=user)

    context = {
        "user":user,
        "transactions":transactions,
        "giftcards":giftcards,
        }
    return render(request, 'core/dashboard.html', context)


def sellcrypto(request):
    return render(request, 'core/sellcrypto.html')

def buycrypto(request):
    return render(request, 'core/buycrypto.html')
