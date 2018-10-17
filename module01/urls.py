from django.urls import path
from module01 import views


urlpatterns = [
    path('', views.index, name='index'),
]


