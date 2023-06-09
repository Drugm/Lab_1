# Generated by Django 3.2.10 on 2021-12-08 12:03

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Город')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('taxi', models.TextField(db_index=True, max_length=350, null=True, verbose_name='Такси')),
                ('adress_city', models.CharField(db_index=True, max_length=100, null=True, verbose_name='Адресс')),
                ('tel', models.IntegerField(db_index=True, null=True, verbose_name='Телефон')),
                ('site', models.URLField(db_index=True, max_length=100, null=True, verbose_name='Сайт')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('kinopoisk', models.IntegerField(null=True, verbose_name='ID Кинопоиск')),
                ('content', models.TextField(blank=True, null=True, verbose_name='О фильме')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/posters/', verbose_name='Постер')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Трейлер')),
                ('country', models.CharField(blank=True, max_length=200, null=True, verbose_name='Страна')),
                ('year', models.DateField(blank=True, null=True, verbose_name='Дата выхода')),
                ('age_limit', models.CharField(blank=True, max_length=200, null=True, verbose_name='Возраст')),
                ('format_3d', models.BooleanField(blank=True, default=False, null=True, verbose_name='Формат 3D')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='Продолжительность')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(blank=True, default=True, null=True, verbose_name='Публикация')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='movie.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['time_create'],
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('price', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цена',
                'ordering': ['price'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Дата показа')),
                ('time', models.TimeField(null=True, verbose_name='Время показа')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.city', verbose_name='Город')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='Фильм')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.price', verbose_name='Цена')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.room', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
                'ordering': ['movie', 'city', 'date', 'time'],
            },
        ),
    ]
