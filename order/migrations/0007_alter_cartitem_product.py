# Generated by Django 5.1.2 on 2024-11-16 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_cartitem_id'),
        ('store', '0009_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='store.product', verbose_name='პროდუქტი'),
        ),
    ]