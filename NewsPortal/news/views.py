from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import New

from datetime import datetime


class NewList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = New
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_pub'
    # queryset = Product.objects.filter(price__lt=150).order_by('name')
    # Указываем имя шаблона, в котором будут все инcтрукции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_pub'] = datetime.utcnow()
        return context


class NewDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = New
    # Используем другой шаблон — product.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'new'
    pk_url_kwarg = 'id'