# Generated by Django 4.0.3 on 2022-08-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orders_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivery',
            field=models.CharField(choices=[('dostavka', 'dostavka'), ('samovizov', 'samovizov')], max_length=20),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_type',
            field=models.CharField(choices=[('click', 'click'), ('payme', 'payme'), ('nalichniy', 'nalichniy')], max_length=20),
        ),
    ]
