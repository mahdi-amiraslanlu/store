# Generated by Django 5.0.7 on 2024-08-04 06:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customer_options_alter_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.BigIntegerField(blank=True, error_messages={'unique': ' A user with this mobile number already exists.'}, null=True, unique=True, validators=[django.core.validators.RegexValidator('^989[0-3,9]\\d{8}$', 'enter a valid mobile number. ')], verbose_name='شماره تماس'),
        ),
    ]