from django.http import JsonResponse
from game.models.color.color import Color

def gett(elem):
    return elem['color_times']


def getinfo(request):
    color=Color.objects.all()
    list=[]
    for i in color:
        json_dict={}
        json_dict['color_name']=i.color_name
        json_dict['color_times']=i.color_times
        list.append(json_dict)
    list.sort(key=gett,reverse=True)

    return JsonResponse(
        
            list, #返回表单内所有的颜色
            safe=False,
        
        
    )
