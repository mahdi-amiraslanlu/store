# Generated by Django 5.0.7 on 2024-08-09 08:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customeruser_options_remove_customeruser_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'مشتری', 'verbose_name_plural': 'مشتری ها'},
        ),
        migrations.AlterModelOptions(
            name='customeruser',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': ' مدیریت ادمین '},
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='مشتری'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='نام'),
        ),
    ]