# Generated by Django 5.1.2 on 2025-02-04 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheltradeAdmin', '0003_cashback_alter_transactioncharge_transactionname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptowallet',
            old_name='crytopName',
            new_name='cryptoName',
        ),
    ]
