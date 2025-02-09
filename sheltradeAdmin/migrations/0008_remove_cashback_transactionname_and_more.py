# Generated by Django 5.1.2 on 2025-02-06 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheltradeAdmin', '0007_alter_cryptowallet_minimumdeposit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashback',
            name='TransactionName',
        ),
        migrations.RemoveField(
            model_name='transactioncharge',
            name='TransactionName',
        ),
        migrations.AlterField(
            model_name='cashback',
            name='amount',
            field=models.PositiveIntegerField(help_text='Percentage(%) per transaction for Airtime, Data, Electric bills, Cable bills'),
        ),
        migrations.AlterField(
            model_name='transactioncharge',
            name='charge',
            field=models.PositiveIntegerField(help_text='Percentage(%) per transaction for Giftcard, Crypto'),
        ),
    ]
