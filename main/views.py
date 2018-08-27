from django.shortcuts import render
from .models import Basket, Pizz, Drink, Potato, Pasta
from django.views import generic

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_pizz=Pizz.objects.all().count()
    num_drink=Drink.objects.all().count()
    
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_pizz':num_pizz,'num_drink':num_drink},
    )

class PizzListView(generic.ListView):
    model = Pizz

class DrinkListView(generic.ListView):
    model = Drink

class PotatoListView(generic.ListView):
    model = Potato

class PastaListView(generic.ListView):
    model = Pasta