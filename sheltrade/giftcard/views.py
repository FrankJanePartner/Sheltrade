from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import GiftCard, BuyGiftCard
from wallet.models import Transaction, Wallet
import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from datetime import datetime
from decimal import Decimal

def buygiftcard(request):
    giftcards = GiftCard.objects.all()

    context = {
        "giftcards":giftcards,
    }
    return render(request, 'giftcard/buygiftcard.html', context)

def sellgiftcard(request):
    return render(request, 'giftcard/sellgiftcard.html')

def add_gift_card(request):
    if request.method == 'POST':
        seller = request.user  # Assuming the user is logged in
        card_type = request.POST.get('card_type')
        card_number = request.POST.get('card_number')
        card_pin = request.POST.get('card_pin')
        card_code = request.POST.get('card_code')
        expiration_date = request.POST.get('expiration_date')
        condition = request.POST.get('condition')
        restrictions = request.POST.get('restrictions')
        price = request.POST.get('price')

        uploaded_image = request.FILES.get('uploaded_image')
        if uploaded_image:
            fs = FileSystemStorage()
            uploaded_image = fs.save(uploaded_image.name, uploaded_image)

        if expiration_date:
            try:
                expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
            except ValueError:
                return render(request, 'add_gift_card.html', {
                    'error': "Invalid date format. Please use YYYY-MM-DD."
                })
        else:
            expiration_date = None  # Set to None if no date is provided

        # Create the GiftCard instance
        gift_card = GiftCard(
            seller=seller,
            card_type=card_type,
            card_number=card_number,
            card_pin=card_pin,
            card_code=card_code,
            expiration_date=expiration_date,
            condition=condition,
            restrictions=restrictions,
            uploaded_image=uploaded_image,
            price=price
        )
        amount= float(price) - 0.01
        gift_card.save()
        
        transaction = Transaction(user=request.user, transaction_type='Sell GiftCard', amount=amount, status="pending")
        transaction.save()

        # ScrapyData = scrape_gift_card_granny(card_type)
        # if ScrapyData:
        #     # Do something with the price info (e.g., update the GiftCard model)
        #     gift_card.price = ScrapyData  # If you want to update the price based on scraping
        #     gift_card.save()

        messages.success(request, f"GiftCard Successfully uploaded")
        return redirect('core:dashboard')

    return render(request, 'add_gift_card.html')

def buy_gift_card(request):
    if request.method == 'POST':
        selected_amount = request.POST.get('card-amount', None)
        giftcard_id = request.POST.get('giftcard-id', None)

        if not selected_amount or not giftcard_id:
            messages.error(request, 'Amount and gift card are required.')
            return redirect('giftcard:buygiftcard')

        try:
            amount = Decimal(selected_amount)
            selected_giftcard = GiftCard.objects.get(id=giftcard_id)

            with transaction.atomic():  # Ensure all-or-nothing for wallet and transaction updates
                guygiftcard = BuyGiftCard(buyer=request.user, gift_card=selected_giftcard)
                guygiftcard.save()

                wallet = Wallet.objects.get(user=request.user)
                total_cost = amount + Decimal('5.00')  # Include processing fee

                if wallet.userBalance < total_cost:
                    messages.error(request, 'Insufficient balance in your wallet.')
                    return redirect('giftcard:buygiftcard')

                wallet.userBalance -= total_cost  # Deduct amount + fee
                wallet.save()  # Save updated wallet balance

                messages.success(request, f'Gift card for {selected_giftcard.card_type} purchased successfully! Total: ${total_cost:.2f}')

                # Log the transaction
                transaction = Transaction(user=request.user, transaction_type='Fund Held', amount=amount, status="pending")
                transaction.save()

            return redirect('core:dashboard')  # Redirect to a success page

        except (ValueError, GiftCard.DoesNotExist):
            messages.error(request, 'Please enter a valid amount or select a gift card.')
            return redirect('giftcard:buygiftcard')

    return redirect('giftcard:buygiftcard')

def scrape_gift_card_granny(card_type):
    # Prepare the search URL for Gift Card Granny
    url = f"https://www.giftcardgranny.com/{card_type.lower().replace(' ', '-')}/"

    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            return None  # Return None if the page cannot be accessed

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the price information (modify the selectors based on the actual HTML structure)
        price_elements = soup.find_all('div', class_='price')  # Adjust class name as necessary
        prices = []

        for price_element in price_elements:
            price_text = price_element.get_text(strip=True)
            prices.append(price_text)

        return prices  # Return the list of prices

    except Exception as e:
        print(f"Error while scraping: {e}")
        return None





# from django.shortcuts import render, redirect
# from .models import GiftCard
# from .utils import validate_gift_card
# from wallet.models import Transaction, Wallet
# from django.contrib.auth.decorators import login_required


# # Create your views here.
# @login_required
# def sellgiftcard(request):
#     if request.method == 'POST':
#         card_number = request.POST.get('card_number')
#         card_pin = request.POST.get('card_pin')
#         amount = request.POST.get('amount')

#         # Validate gift card using Zendit API
#         validation_result = validate_gift_card(card_number, card_pin)
#         if validation_result.get('status') == 'valid':
#             # Save to database if valid
#             gift_card = GiftCard.objects.create(
#                 user=request.user,
#                 card_number=card_number,
#                 card_pin=card_pin,
#                 amount=amount,
#                 status='on the market'
#             )
#             return redirect('core:dashboard')
#         else:
#             return render(request, 'sellgiftcard.html', {'error': 'Invalid Gift Card'})

#     return render(request, 'sellgiftcard.html')



# @login_required
# def buygiftcard(request, gift_card_id):
#     gift_card = GiftCard.objects.get(id=gift_card_id)

#     # Re-validate the gift card using Zendit API before purchase
#     validation_result = validate_gift_card(gift_card.card_number, gift_card.card_pin)
#     if validation_result.get('status') != 'valid':
#         gift_card.status = 'invalid'
#         gift_card.save()
#         # Notify seller
#         # (Implement notification logic)
#         return render(request, 'buygiftcard.html', {'error': 'Gift card no longer valid'})

#     # Check buyer's wallet balance
#     wallet = Wallet.objects.get(user=request.user)
#     if wallet.balance < gift_card.amount:
#         return render(request, 'buygiftcard.html', {'error': 'Insufficient balance'})

#     # Process the transaction
#     wallet.balance -= gift_card.amount
#     wallet.save()

#     # Create transaction records for buyer and seller
#     Transaction.objects.create(user=request.user, transaction_type='Purchased Gift Card', transaction_price=gift_card.amount, status='approved')
#     seller_wallet = Wallet.objects.get(user=gift_card.user)
#     seller_wallet.balance += gift_card.amount  # Subtract any platform fees
#     seller_wallet.save()
#     Transaction.objects.create(user=gift_card.user, transaction_type='Sold Gift Card', transaction_price=gift_card.amount, status='approved')

#     # Update gift card status
#     gift_card.status = 'sold'
#     gift_card.save()

#     # Notify buyer and seller via email
#     # (Implement email sending logic)

#     return redirect('core:dashboard')
