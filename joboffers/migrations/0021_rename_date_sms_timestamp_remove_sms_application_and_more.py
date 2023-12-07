# Generated by Django 4.2.3 on 2023-11-28 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0020_remove_sms_company_remove_sms_user_sms_receiver_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sms',
            old_name='date',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='sms',
            name='application',
        ),
        migrations.RemoveField(
            model_name='sms',
            name='message',
        ),
        migrations.AddField(
            model_name='sms',
            name='content',
            field=models.TextField(blank=True, default='Default content', null=True),
        ),
    ]
