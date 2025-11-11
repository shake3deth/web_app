from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("mypage/", views.mypage, name = "mypage"),
    path("game/", views.game , name = "game")
]