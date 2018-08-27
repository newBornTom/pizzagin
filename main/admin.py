from django.contrib import admin
from .models import Basket, Pizz, Drink, Potato, Pasta

# Define the admin class
class BasketAdmin(admin.ModelAdmin):
    pass
admin.site.register(Basket, BasketAdmin)
# Register the admin class with the associated model



@admin.register(Pizz)
class PizzAdmin(admin.ModelAdmin):
    list_display = ('title', 'pizzphoto', 'aboutpizz', 'price')

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'drinkphoto', 'price')

@admin.register(Potato)
class PotatoAdmin(admin.ModelAdmin):
    list_display = ('title', 'potatophoto', 'price')

@admin.register(Pasta)
class PastaAdmin(admin.ModelAdmin):
    list_display = ('title', 'pastaphoto', 'price')
   # readonly_fields = ('drinkphoto',)
   # fields =['drinkphoto']

#admin.site.register(Basket)
#admin.site.register(Pizz)

# Register your models here.
