# Generated by Django 5.0 on 2024-10-30 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_price',
            new_name='amount',
        ),
    ]