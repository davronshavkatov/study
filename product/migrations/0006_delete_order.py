# Generated by Django 4.0.3 on 2022-08-05 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_category_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
