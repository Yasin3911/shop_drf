# Generated by Django 5.1.7 on 2025-03-27 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_is_active_productline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productline',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_line', to='product.product'),
        ),
    ]
