# Generated by Django 4.0.5 on 2022-07-12 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_coupon_order_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Order'},
        ),
    ]
