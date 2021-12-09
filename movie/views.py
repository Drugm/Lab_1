from datetime import datetime, timedelta

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import FormCity
from .models import *

'''
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить ", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]
'''
# menu = [{'title': "О сайте", 'url_name': 'about'}]
menu = [{'title': "О сайте", 'url_name': 'about'}]


def index(request):
    #  Get Cookie
    if 'city' in request.COOKIES:
        slug_city = request.COOKIES["city"]
        dt = datetime.now()
        date = dt.strftime('%d%m%y')
        return redirect('/' + slug_city + '/' + date)
    else:
        context = {
            'menu': menu,
            'change_city': 'Выберите город',
            'title': 'Выберите город',
        }
        return render(request, 'movie/index.html', context=context)


def about(request):
    context = {'menu': menu, 'title': 'О сайте'}
    return render(request, 'movie/about.html', context)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


'''
def show_post(request, post_id):
    return HttpResponse(f"Отображение фильма с id = {post_id}")
'''


def show_post(request, post_id):
    post = Movie.objects.get(id=post_id)
    context = {
        'post_id': post_id,
        'post': post,
        'menu': menu,
    }
    response = render(request, 'movie/video.html', context=context)
    return response


def change_city(request, city_slug):
    #   try:
    posts_today = Show.objects.filter(city__slug=city_slug, date=datetime.now())
    city = City.objects.get(slug=city_slug)
    context = {
        'posts': posts_today,
        'menu': menu,
        'title': city,
        'city_selected': city_slug,
    }
    response = render(request, 'movie/index.html', context=context)  # django.http.HttpResponse
    response.set_cookie(key='city', value=city_slug, max_age=63072000)  # Куки город
    return response


# except BaseException:
#    raise Http404()


def show_by_date(request, city_slug, dmy):
    #   try:
    date = datetime.strptime(dmy, '%d%m%y')
    now_date = datetime.now()
    posts = Show.objects.order_by(
        'movie'
    ).filter(
        city__slug=city_slug, date=date
    )
    city = City.objects.get(slug=city_slug)
    dates = Show.objects.order_by(
        'date'
    ).filter(
        date__range=[datetime.now(), datetime.now() + timedelta(days=7)], city__slug=city_slug
    )
    print(posts)
    context = {
        'posts': posts,
        'dates': dates,
        'now_date': now_date,
        'menu': menu,
        'title': city,
        'taxi': city.taxi,
        'tel': city.tel,
        'adress_sity': city.adress_city,
        'city_selected': city_slug,
        'date_selected': dmy,
    }
    response = render(request, 'movie/index.html', context=context)  # django.http.HttpResponse
    response.set_cookie(key='city', value=city_slug, max_age=63072000)  # Куки город
    return response


#  except BaseException:
#     raise Http404()


