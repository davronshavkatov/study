# Generated by Django 4.0.3 on 2022-08-07 10:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orders_delivery_alter_orders_payment_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='product_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='current_time',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='filial',
        ),
        migrations.AddField(
            model_name='orders',
            name='filial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.filial'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
