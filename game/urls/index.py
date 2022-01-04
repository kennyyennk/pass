
from django.urls import path,include
from game.views.index import index,ground
from game.views.getinfo import getinfo
from game.views.save_data import Save_data

urlpatterns = [
    path("",index,name="index"),
    path('ground/',ground,name="ground"),
    path('getinfo/',getinfo,name="views_getinfo"),
]

