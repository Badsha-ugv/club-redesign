# Generated by Django 4.2.2 on 2023-08-03 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_alter_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tag',
            field=models.CharField(blank=True, help_text='category or subcategory name', max_length=100, null=True),
        ),
    ]