# Generated by Django 4.2.3 on 2023-11-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0022_sms_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='sms',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
