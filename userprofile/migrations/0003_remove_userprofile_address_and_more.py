# Generated by Django 4.2.1 on 2023-05-27 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_address_userprofile_whatsapp_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='WhatsApp_No',
        ),
    ]
