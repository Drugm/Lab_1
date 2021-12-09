from datetime import datetime, date, timedelta

from django import template
from movie.models import *

register = template.Library()


@register.inclusion_tag('movie/list_cities.html')
def show_cities(city_selected):
    now_date = datetime.now()
    cities = City.objects.all()
    return {"cities": cities, "now_date": now_date, "city_selected": city_selected}


@register.inclusion_tag('movie/list_dates.html')
def show_dates(date_selected):
    now_date = datetime.now()
    dates = Show.objects.order_by(
        'date'
    ).filter(
        date__range=[datetime.now(), datetime.now() + timedelta(days=7)]
    )
    return {"dates": dates, "now_date": now_date, "date_selected": date_selected}
