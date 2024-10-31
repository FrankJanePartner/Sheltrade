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
    if created:
        user = instance.user
        giftcard = GiftCard.objects.filter(seller=user).first()
        giftcardBuyer = BuyGiftCard.objects.filter(buyer=user).first()

        # Ensure that the user has both a gift card and a buyer record
        if not giftcard or not giftcardBuyer:
            # Log an error or handle it appropriately
            return

        userBalance = Wallet.objects.get(user=user)

        if instance.status == 'Approved':
            if instance.transaction_type == 'Deposit':
                userBalance.userBalance += instance.amount
            elif instance.transaction_type == 'Withdrawal':
                userBalance.userBalance -= instance.amount
            elif instance.transaction_type == 'SellGift Card':
                giftcard.status = "listed"
            elif instance.transaction_type == 'Fund Held':
                # Mark the gift card as sold
                giftcard.status = "Sold"
                
                # Update seller's wallet
                seller_wallet = Wallet.objects.get(user=giftcard.seller)
                seller_wallet.userBalance += instance.amount  # Update the seller's balance
                
                # Release the escrow status
                giftcard.escrow_status = "released"

                # Save both wallets and the gift card
                seller_wallet.save()
            
            # Save the user's wallet and gift card changes
            userBalance.save()
            giftcard.save()

        elif instance.status == 'rejected' and instance.transaction_type == 'Fund Held':
            giftcard.status = "invalid"
            giftcardBuyer.userBalance += instance.amount
            giftcard.escrow_status = "refunded"

            # Save updated states
            userBalance.save()
            giftcardBuyer.save()
            giftcard.save()

# @receiver(post_save, sender=Earned)
# def handle_User_Earning(sender, instance, created, **Kwargs):
#     user = instance.user
#     profile = Profile.objects.get(user=user)