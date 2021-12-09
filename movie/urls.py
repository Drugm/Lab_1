from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('<slug:city_slug>/', change_city, name='city'),
    path('<slug:city_slug>/<str:dmy>', show_by_date, name='show_by_date'),
    ]
