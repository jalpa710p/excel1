# Generated by Django 4.2.6 on 2024-03-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelapp', '0003_remove_mymodel_otp_mymodel_email_otp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
