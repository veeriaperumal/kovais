# Generated by Django 5.0.7 on 2024-10-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userdetails_premium_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='sucess',
            field=models.BooleanField(default=False),
        ),
    ]