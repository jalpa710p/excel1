# Generated by Django 4.2.6 on 2024-03-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelapp', '0005_mymodel_is_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lgform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
    ]