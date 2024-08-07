# Generated by Django 4.2.15 on 2024-08-07 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True, verbose_name='تعداد')),
            ],
            options={
                'verbose_name': ' کارت',
                'verbose_name_plural': ' کارت ها ',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان سفارش')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='قیمت کل')),
            ],
            options={
                'verbose_name': ' سفارش ',
                'verbose_name_plural': 'سفارشات',
                'ordering': ['-order_date'],
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name=' محصولات ')),
            ],
            options={
                'verbose_name': ' علاقه مندی ',
                'verbose_name_plural': 'علاقه مندی ها ',
            },
        ),
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name=' تعداد ')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='قیمت ')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name=' سفارشات ')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name=' محصولات ')),
            ],
            options={
                'verbose_name': ' آیتم سفارش',
                'verbose_name_plural': 'آیتم های سفارشات',
            },
        ),
    ]
