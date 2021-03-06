# Generated by Django 3.0.2 on 2020-02-02 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_auto_20200131_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anon',
            options={'verbose_name': 'Анонс', 'verbose_name_plural': 'Анонсы'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='plase',
            options={'verbose_name': 'Интерестное место', 'verbose_name_plural': 'Интерестные места'},
        ),
        migrations.RemoveField(
            model_name='anon',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='anon',
            name='date',
            field=models.CharField(default=1, max_length=200, verbose_name='Дата тура'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anon',
            name='description',
            field=models.TextField(blank=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='anon',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='anon',
            name='photo_main',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='anon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='img/gallery_pics', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='plase',
            name='description',
            field=models.TextField(blank=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='plase',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='img/photo_main_pics', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='plase',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='plase',
            name='post_title',
            field=models.CharField(max_length=200, verbose_name='Пост-заголовок'),
        ),
        migrations.AlterField(
            model_name='plase',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
