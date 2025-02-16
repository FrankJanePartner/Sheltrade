# Generated by Django 5.0 on 2025-01-27 23:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(help_text='Brand/retailer name e.g., Amazon, Steam', max_length=50)),
                ('card_number', models.CharField(blank=True, max_length=30, null=True)),
                ('card_pin', models.CharField(blank=True, max_length=30, null=True)),
                ('card_code', models.CharField(blank=True, max_length=20, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('condition', models.CharField(blank=True, help_text='Condition of the gift card (new, used, partially used)', max_length=20, null=True)),
                ('restrictions', models.TextField(blank=True, help_text='Any specific terms or restrictions', null=True)),
                ('uploaded_image', models.ImageField(blank=True, null=True, upload_to='gift_cards/')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending Verification'), ('invalid', 'Invalid'), ('listed', 'Listed for Sale'), ('Sold', 'Sold')], default='listed', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuyGiftCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escrow_status', models.CharField(choices=[('held', 'Held'), ('released', 'Released'), ('refunded', 'Refunded')], default='held', max_length=10)),
                ('bought_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bought_cards', to=settings.AUTH_USER_MODEL)),
                ('gift_card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bought', to='giftcard.giftcard')),
            ],
        ),
    ]
