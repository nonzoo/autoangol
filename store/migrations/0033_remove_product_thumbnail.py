# Generated by Django 4.2.1 on 2023-07-04 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_alter_product_condition_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]
