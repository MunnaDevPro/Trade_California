from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("subscribe/", views.subscribe_newsletter, name="subscribe_newsletter"),
    path("api/chat/", views.ai_chat, name="ai_chat"),
]
