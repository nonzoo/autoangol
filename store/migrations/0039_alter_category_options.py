# Generated by Django 4.2.1 on 2023-09-29 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_alter_category_options_subcategory_title_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name_plural': 'Category/Industry'},
        ),
    ]
