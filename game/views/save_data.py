from game.models.color.color import Color
from django.shortcuts import render

def Save_data(request):
    if  request.method == 'POST':
        color =request.POST.get('color')
        
    if(Color.objects.filter(color_name=color).exists()):
        tempcolor=Color.objects.get(color_name=color)
        tempcolor.color_times+=1
        tempcolor.save()
    else:
        tempcolor=Color(
        color_name=color,
        color_times=1
        )
        tempcolor.save()

    return
