# Generated by Django 5.0 on 2024-10-31 07:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0002_rename_date_added_giftcard_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyGiftCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bought_cards', to=settings.AUTH_USER_MODEL)),
                ('gift_card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bought', to='giftcard.giftcard')),
            ],
        ),
    ]
