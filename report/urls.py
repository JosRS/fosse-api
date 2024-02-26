from . import views
from django.urls import path

index = ''

urlpatterns = [
    path(index, views.hello)
]