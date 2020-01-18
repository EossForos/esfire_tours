# Generated by Django 3.0.2 on 2020-01-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_plase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
