from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Transaction,  Wallet
from giftcard.models import GiftCard, BuyGiftCard



@receiver(post_save, sender=User)
def create_user_transaction(sender, instance, created, **kwargs):
    if created:
        # Create a Transaction instance for the new user
        Wallet.objects.create(user=instance)
          # Adjust the amount or any other fields as necessary



@receiver(post_save, sender=Transaction)
def handle_User_transactions(sender, instance, created, **kwargs):
    user = instance.user
    userBalance = Wallet.objects.get(user=user)

    # Get the related BuyGiftCard instances for the user
    giftcardBuyers = BuyGiftCard.objects.filter(buyer=user)

    # Check if there are any BuyGiftCard instances
    if not giftcardBuyers.exists():
        print("No BuyGiftCard instances for this user.")
        return  # Early exit if no BuyGiftCard records found

    for giftcardBuyer in giftcardBuyers:
        seller = giftcardBuyer.gift_card.seller
        sellerBalance = Wallet.objects.get(user=seller)
        

        # Proceed with the transaction logic based on instance.status and transaction_type
        if instance.status == 'Approved':
            if instance.transaction_type == "Deposit":
                userBalance.userBalance += instance.amount
                userBalance.save()
            elif instance.transaction_type == 'Withdrawal':
                userBalance.userBalance -= instance.amount
                userBalance.save()
            elif instance.transaction_type == 'Sell Giftcard':
                giftcardBuyer.gift_card.status = "listed"
                giftcardBuyer.gift_card.save()  # Save the updated gift card status
            elif instance.transaction_type == 'Buy Giftcard':
                giftcardBuyer.gift_card.status = "Sold"
                for giftcardBuyer in giftcardBuyers:
                    seller = giftcardBuyer.gift_card.seller
                    sellerBalance = Wallet.objects.get(user=seller)
                
                giftcardBuyer.escrow_status = "Sold"
                sellerBalance.userBalance += instance.amount
                sellerBalance.save()
                transaction = Transaction(user=seller, transaction_type='Sell Giftcard', amount=instance.amount, status="Approved")
                transaction.save()
            else:
                pass

        elif instance.status == 'Rejected':
            if instance.transaction_type == 'Buy Giftcard':
                giftcardBuyer.gift_card.status = "Sold"
                for giftcardBuyer in giftcardBuyers:
                    seller = giftcardBuyer.gift_card.seller
                    sellerBalance = Wallet.objects.get(user=seller)
                
                giftcardBuyer.escrow_status = "Sold"
                sellerBalance.userBalance += instance.amount
                sellerBalance.save()
                transaction = Transaction(user=seller, transaction_type='Sell Giftcard', amount=instance.amount, status="Approved")
                transaction.save()