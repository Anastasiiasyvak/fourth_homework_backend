from django.urls import path
from . import views


urlpatterns = [
    path("hello", views.sayHello),
    path("image", views.sendImage),
    path("html", views.sendHtml),
    path("json", views.sendJson),
    # path("hello/big"), views.sayBig),
    path("hello/custom", views.SayBigCustom),

    path("crud/", views.handleCrud),

    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.get_cookie),
    path('ws/', views.my_websocket)
]
