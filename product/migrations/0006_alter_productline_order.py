# Generated by Django 5.1.7 on 2025-03-28 12:34

import product.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productline_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productline',
            name='order',
            field=product.fields.OrderField(blank=True, null=True),
        ),
    ]
