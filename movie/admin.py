from datetime import timedelta

import requests
import wget
from django.contrib import admin
from django.db.models.functions import Lower

from .models import *


def kinopoisk(modeladmin, request, queryset):
    # клонирование выбранных
    for movie in queryset:
        id_kinopoisk = movie.kinopoisk
        token_kinopoisk_cloud = 'a56e0741698abf3ef52bf911c9a26793'
        response = requests.get(f'https://api.kinopoisk.cloud/movies/{id_kinopoisk}/token/{token_kinopoisk_cloud}')
        json_response = response.json()
        title = json_response["title"]
        movie.title = title

        description = json_response["description"]
        movie.content = description
        poster = json_response["poster"]
        print(poster)
        r = requests.get('http:' + str(poster))
        print(r)
        with open(f'media/photos/posters/{id_kinopoisk}.jpg', 'wb') as f: f.write(r.content)
        poster = f'/photos/posters/{id_kinopoisk}.jpg'

        movie.photo = poster
        trailer = json_response["trailer"]
        movie.video = trailer
        age = json_response["age"]
        movie.age_limit = age
        # movie.pk = None
        movie.save()


kinopoisk.short_description = "Кинопоиск"


class MovieAdmin(admin.ModelAdmin):
    actions = [kinopoisk]
    list_display = ('id', 'title', 'time_create', 'format_3d', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


def dublicate_ad(modeladmin, request, queryset):
    # клонирование выбранных
    for show in queryset:
        show.pk = None
        show.save()


def dublicate_ad_new_day(modeladmin, request, queryset):
    # клонирование выбранных
    for show in queryset:
        show.date = show.date + timedelta(days=1)
        show.pk = None
        show.save()


def dublicate_ad_new_week(modeladmin, request, queryset):
    # клонирование выбранных
    for show in queryset:
        for number in range(6):
            show.date = show.date + timedelta(days=1)
            show.pk = None
            show.save()


class ShowAdmin(admin.ModelAdmin):
    actions = [dublicate_ad, dublicate_ad_new_day, dublicate_ad_new_week]

    list_display = ("city", "movie", "date", "time")
    list_filter = ("city", "movie", "date", "time", "price", "room")


    dublicate_ad.short_description = "Дублировать объект"
    dublicate_ad_new_day.short_description = "Дублировать объект на завтра"
    dublicate_ad_new_week.short_description = "Дублировать объект на наделю"


'''
    def get_ordering(self, request):
                return [Lower('movie')]  # sort case insensitive
'''

admin.site.register(Movie, MovieAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Price)
admin.site.register(Room)
admin.site.register(Genre)
admin.site.register(Show, ShowAdmin)

admin.site.site_title = 'Админ-панель сайта кинотеатра'
admin.site.site_header = 'Админ-панель сайта о кинотеатра'
