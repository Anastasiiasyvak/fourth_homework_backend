from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os

from django.http import HttpResponse, JsonResponse, FileResponse


def set_cookie(request):
    response = HttpResponse("Cookie set!")
    response.set_cookie('my_cookie', 'Hello from server')
    response.set_cookie('my_cookieHttpOnly', 'Hello from server', httponly=True)
    return response


def get_cookie(request):
    print(request.COOKIES)
    # print(request.META)
    my_cookie_value = request.COOKIES.get('my_cookie', 'Cookie not set')
    return HttpResponse(f"Value of my_cookie: {my_cookie_value}")


def sayHello(request):
    return HttpResponse("Hello, Django!")


def sendJson(request):
    return JsonResponse({'message': "JSON received"})


def sendHtml(request):
    return render(request, 'hello.html')


def sendImage(request):
    image_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'image.jpg')
    return FileResponse(open(image_path, 'rb'), content_type='image/jpg')


def SayBigCustom(request):
    return render(request), {'username': 'Beauty', 'items': [{'name': 'Taras'}, {'name': 'Jessy'}
                                       ]}


def getSmth(request):
    data = {'message': 'GET request received'}
    return JsonResponse(data)


def postSmth(request):
    try:
        data = json.loads(request.body)
        field_value = data.get('field_name', None)
        return JsonResponse(data)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data received'}, status=400)


def putSmth(request):
    data = {'message': 'PUT request received'}
    return JsonResponse(data)


def deleteSmth(request, *args, **kwargs):
    data = {'message': 'DELETE request received'}
    return JsonResponse(data)


@csrf_exempt
def handleCrud(request):
    if request.method == 'GET':
        return getSmth(request)
    elif request.method == 'POST':
        return postSmth(request)
    elif request.method == 'PUT':
        return putSmth(request)
    elif request.method == 'DELETE':
        return deleteSmth(request)
    else:
        return JsonResponse({'message': 'Unsupported HTTP method'})


def my_websocket(request):
    return render(request, 'websocket.html')
