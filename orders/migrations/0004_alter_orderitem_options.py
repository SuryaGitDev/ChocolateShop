# Generated by Django 4.0.5 on 2022-07-10 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'order'},
        ),
    ]
