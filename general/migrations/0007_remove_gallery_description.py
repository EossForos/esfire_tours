# Generated by Django 3.0.2 on 2020-01-18 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='description',
        ),
    ]
