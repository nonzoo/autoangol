# Generated by Django 4.2.1 on 2023-07-06 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0035_product_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Used', 'Used')], max_length=50, null=True),
        ),
    ]
