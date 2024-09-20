from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=15)
#     address = models.TextField()
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=10)
#     country = models.CharField(max_length=100)
#     profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
#     id_card = models.ImageField(upload_to='id_cards', blank=True, null=True)
#     proof_of_address = models.ImageField(upload_to='proof_of_addresses', blank=True, null=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     is_verified = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_deleted = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

# class Wallet(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     wallet_address = models.CharField(max_length=100)
#     wallet_private_key = models.CharField(max_length=100)
#     wallet_public_key = models.CharField(max_length=100)
#     wallet_seed_phrase = models.CharField(max_length=100)
#     wallet_pin = models.CharField(max_length=100)
#     wallet_mnemonic = models.CharField(max_length=100)
#     wallet_qr_code = models.ImageField(upload_to='wallet_qr_codes', blank=True, null=True)
#     wallet_date_created = models.DateTimeField(auto_now_add=True)

