from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Notification
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
    notifications = Notification.objects.filter(user=request.user)
    unread_count = notifications.filter(is_read=False).count()

    context = {
        "user":user,
        "transactions":transactions,
        'notifications': notifications,
        'unread_count': unread_count
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

            Notification.objects.create(
                user=user,
                title='Your Preferred Currency Set',
                content="Your Preferred Currency Has been set"
            )

            messages.info(request, 'Your Preferred Currency Has been set.')
        else:
            # Update the preferred currency
            profile.preferredCurrency = currency
            profile.save()

            Notification.objects.create(
                user=user,
                title='Your Preferred Currency Updated',
                content="Your Preferred Currency Has been Updated"
            )

            messages.info(request, 'Your Preferred Currency Has been Updated.')
        return redirect('core:profile')
        # Handle the deposit logic here using the narration

@login_required
def notification(request):
    notifications = Notification.objects.filter(user=request.user)
    unread_count = notifications.filter(is_read=False).count()
    return render(request, 'core/notification.html', {'notifications': notifications, 'unread_count': unread_count})

@login_required
def notification_detail(request, slug):
    notification = get_object_or_404(Notification, slug=slug)
    # Mark as read when viewed
    if not notification.is_read:
        notification.mark_as_read()
    context = {'notification': notification}
    return render(request, 'core/notificationDetail.html', context)


@login_required
def mark_all_as_read(request):
    """Marks all notifications as read."""
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return redirect('core:notification')


def settings(request):
    return render(request, 'profile/settings.html')