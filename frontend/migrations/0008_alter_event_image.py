# Generated by Django 4.2.2 on 2023-08-02 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='def-event.jpg', upload_to='event/'),
        ),
    ]