# Generated by Django 4.2.2 on 2023-08-02 23:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_sliderimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('subtitle', models.CharField(blank=True, max_length=400)),
                ('desc', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='event/')),
                ('event_staus', models.CharField(choices=[('UPCOMMING', 'UPCOMMING'), ('RUNNING', 'RUNNING'), ('EXPIRED', 'EXPIRED')], default='UPCOMMING', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
