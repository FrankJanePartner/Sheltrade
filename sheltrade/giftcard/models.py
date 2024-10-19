from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GiftCard(models.Model):
    CARD_TYPE_CHOICES = [
        ('amazon', 'Amazon'),
        ('itunes', 'iTunes'),
        ('google-play', 'Google Play'),
        ('steam', 'Steam'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=50, choices=CARD_TYPE_CHOICES, default='other', blank=True)
    other_card_type = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=100)
    card_pin = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_image = models.ImageField(upload_to='gift_cards/')
    status = models.CharField(max_length=20, choices=[('on the market', 'On the Market'), ('sold', 'Sold')], default='on the market')
    date_added = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.user.username



    
