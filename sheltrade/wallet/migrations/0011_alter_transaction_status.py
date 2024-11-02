# Generated by Django 5.0 on 2024-11-01 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0010_rename_bankname_withdrawalaccount_account_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
    ]
