# Generated by Django 4.2.2 on 2023-07-17 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]