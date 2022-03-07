from django.urls import path
from . import views

app_name = 'ssafy'

urlpatterns = [
    # ssafy/ping/ => ping()
    path('ping/', views.ping, name='ping'),
    # ssafy/pong/ => pong()
    path('pong/', views.pong, name='pong'),
]
