from django.urls import path
import views


urlpatterns = [
    path("hello", views.sayHello),
    path("image", views.sendImage),
    path("html", views.sendHtml),
    path("json", views.sendJson),
    # path("hello/big"), views.sayBig),
    path("hello/custom", views.SayBigCustom),

    path("crud/", views.handleCrud)

]
