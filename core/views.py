from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from wallet.models import Transaction, Wallet
from django.contrib import messages
from giftcard.models import GiftCard

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
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
        }
    return render(request, 'core/dashboard.html', context)

@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.filter(user=user)
    return render(request, 'profile/profile.html', {"profile":profile})

@login_required
def preferred_currency(request):
    if request.method == "POST":
        currency = request.POST.get("currency")  # Get currency from POST data
        user = request.user

        # Check if the Profile exists
        profile = Profile.objects.filter(user=user).first()
        if not profile:
            # Create a Profile if it doesn't exist
            profile = Profile.objects.create(user=user, preferredCurrency=currency)
            profile.save()

            messages.info(request, 'Your Preferred Currency Has been set.')
        else:
            # Update the preferred currency
            profile.preferredCurrency = currency
            profile.save()

            messages.info(request, 'Your Preferred Currency Has been set.')
        return redirect('core:profile')
        # Handle the deposit logic here using the narration


def notification(request):
    return render(request, 'core/notification.html')

def settings(request):
    return render(request, 'profile/settings.html')