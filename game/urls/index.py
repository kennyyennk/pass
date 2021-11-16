
from django.urls import path,include
from game.views.index import index,ground


urlpatterns = [
    path("",index,name="index"),
    path('ground/',ground,name="ground"),
]

