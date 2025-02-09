# Generated by Django 5.0 on 2025-01-28 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheltradeAdmin', '0002_transactioncharge'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransactionName', models.CharField(help_text='E.g.: Airtime, Data, Electric bills, Cable bills', max_length=255)),
                ('amount', models.PositiveIntegerField(help_text='Percentage(%) per transaction')),
            ],
            options={
                'verbose_name': 'Cash Back',
                'verbose_name_plural': 'Cash Backs',
            },
        ),
        migrations.AlterField(
            model_name='transactioncharge',
            name='TransactionName',
            field=models.CharField(help_text='E.g.: Giftcard, Crypto', max_length=255),
        ),
    ]
