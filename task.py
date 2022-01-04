from game.models.color.color import Color


def task():
    print('cnm')
    Color.objects.all().delete()
    return
