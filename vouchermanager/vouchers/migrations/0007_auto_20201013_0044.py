# Generated by Django 3.1.2 on 2020-10-13 00:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0006_auto_20201013_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='remaining',
            field=models.PositiveSmallIntegerField(default=3, validators=[django.core.validators.MaxValueValidator(3)]),
        ),
    ]
