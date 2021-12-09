from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Movie(models.Model):
    title = models.CharField(max_length=100,  null=True, verbose_name="Название")
    kinopoisk = models.IntegerField(null=True, verbose_name="ID Кинопоиск")
    content = models.TextField(blank=True, null=True, verbose_name="О фильме")
    photo = models.ImageField(upload_to="photos/posters/", blank=True, null=True, verbose_name="Постер")
    video = EmbedVideoField(blank=True, null=True, verbose_name='Трейлер')
    country = models.CharField(max_length=200, null=True, blank=True, verbose_name='Страна')
    year = models.DateField( null=True, blank=True, verbose_name="Дата выхода")
    age_limit = models.CharField(max_length=200, null=True, blank=True, verbose_name="Возраст")
    format_3d = models.BooleanField(null=True, blank=True, default=False, verbose_name="Формат 3D")
    duration = models.IntegerField(null=True, blank=True, verbose_name="Продолжительность")
    time_create = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, null=True, blank=True, verbose_name="Публикация")
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Жанр")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['time_create']


class City(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Город")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    taxi = models.TextField(max_length=350, db_index=True, null=True, verbose_name="Такси")
    adress_city = models.CharField(max_length=100, db_index=True, null=True, verbose_name="Адресс")
    tel = models.IntegerField(db_index=True, null=True, verbose_name="Телефон")
    site = models.URLField(max_length=100, db_index=True, null=True, verbose_name="Сайт")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('city', kwargs={'city_id': self.pk})
        return reverse('city', kwargs={'city_slug': self.slug})

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['id']


class Price(models.Model):
    price = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цена'
        ordering = ['price']


class Room(models.Model):
    room = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.room)

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Genre(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Жанр")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Show(models.Model):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name="Город")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, verbose_name="Фильм")
    price = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True, verbose_name="Цена")
    date = models.DateField(null=True, verbose_name="Дата показа")
    time = models.TimeField(null=True, verbose_name="Время показа")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, to_field="room", verbose_name="Зал")

    class Meta:
        # unique_together = (("room", "date", "movie"),)
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
        ordering = ['movie', 'city', 'date', 'time']

    def __str__(self):
        return str(self.date) + " | " + str(self.time) + " | " + str(self.movie) + " | " + str(self.room) + " | " + str(
            self.city) + " | " + str(self.price) + "₽"

    #   def get_absolute_url(self):
    #    return reverse('show_by_date', kwargs={'show_id': self.pk})
