# Generated by Django 5.1.2 on 2025-02-04 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_rename_adress_useraddress_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraddress',
            options={'ordering': ['id'], 'verbose_name': 'UserAddress', 'verbose_name_plural': 'UserAddresses'},
        ),
    ]
