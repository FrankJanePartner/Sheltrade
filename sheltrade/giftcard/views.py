from django.shortcuts import render, redirect
from .models import GiftCard
from .utils import validate_gift_card
from wallet.models import Transaction, Wallet
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def sellgiftcard(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        card_pin = request.POST.get('card_pin')
        amount = request.POST.get('amount')

        # Validate gift card using Zendit API
        validation_result = validate_gift_card(card_number, card_pin)
        if validation_result.get('status') == 'valid':
            # Save to database if valid
            gift_card = GiftCard.objects.create(
                user=request.user,
                card_number=card_number,
                card_pin=card_pin,
                amount=amount,
                status='on the market'
            )
            return redirect('core:dashboard')
        else:
            return render(request, 'sellgiftcard.html', {'error': 'Invalid Gift Card'})

    return render(request, 'sellgiftcard.html')



@login_required
def buygiftcard(request, gift_card_id):
    gift_card = GiftCard.objects.get(id=gift_card_id)

    # Re-validate the gift card using Zendit API before purchase
    validation_result = validate_gift_card(gift_card.card_number, gift_card.card_pin)
    if validation_result.get('status') != 'valid':
        gift_card.status = 'invalid'
        gift_card.save()
        # Notify seller
        # (Implement notification logic)
        return render(request, 'buygiftcard.html', {'error': 'Gift card no longer valid'})

    # Check buyer's wallet balance
    wallet = Wallet.objects.get(user=request.user)
    if wallet.balance < gift_card.amount:
        return render(request, 'buygiftcard.html', {'error': 'Insufficient balance'})

    # Process the transaction
    wallet.balance -= gift_card.amount
    wallet.save()

    # Create transaction records for buyer and seller
    Transaction.objects.create(user=request.user, transaction_type='Purchased Gift Card', transaction_price=gift_card.amount, status='approved')
    seller_wallet = Wallet.objects.get(user=gift_card.user)
    seller_wallet.balance += gift_card.amount  # Subtract any platform fees
    seller_wallet.save()
    Transaction.objects.create(user=gift_card.user, transaction_type='Sold Gift Card', transaction_price=gift_card.amount, status='approved')

    # Update gift card status
    gift_card.status = 'sold'
    gift_card.save()

    # Notify buyer and seller via email
    # (Implement email sending logic)

    return redirect('core:dashboard')
