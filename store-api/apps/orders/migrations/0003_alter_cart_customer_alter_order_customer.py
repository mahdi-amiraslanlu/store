# Generated by Django 5.0.7 on 2024-08-09 07:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
        ('users', '0006_alter_customeruser_options_remove_customeruser_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customer', verbose_name='مشتری ها '),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customer', verbose_name=' مشتری '),
        ),
    ]
