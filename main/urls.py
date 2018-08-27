from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('drink', views.DrinkListView.as_view(), name='drink'),
    path('potato', views.PotatoListView.as_view(), name='potato'),
    path('pasta', views.PastaListView.as_view(), name='pasta'),
    
] 