# Generated by Django 5.0.7 on 2024-08-07 11:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0006_alter_payment_customer_alter_shipment_customer_and_more'),
        ('orders', '0005_alter_order_options'),
        ('products', '0004_alter_category_options_alter_product_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='مشتری ها '),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name=' محصولات '),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=' مشتری '),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='financial.payment', verbose_name=' پرداخت '),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial.shipment', verbose_name=' حمل و نقل '),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name=' سفارشات '),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name=' محصولات '),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='quantity',
            field=models.IntegerField(verbose_name=' تعداد '),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name=' محصولات '),
        ),
    ]
