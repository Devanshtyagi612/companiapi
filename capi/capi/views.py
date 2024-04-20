from django.http import HttpResponse,JsonResponse


def home_page(request):
    print("home page")
    f=['tyagi','ankur','ishan']
    return JsonResponse(f,safe=False)