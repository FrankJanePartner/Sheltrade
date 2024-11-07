# Generated by Django 5.0 on 2024-10-31 01:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_withdrawalaccount_delete_withdrawalaccout'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawalaccount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawal_accounts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acount_name', models.CharField(max_length=50)),
                ('acount_number', models.CharField(max_length=50)),
                ('BankName', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawal', to='wallet.transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]