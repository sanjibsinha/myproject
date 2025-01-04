from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Map the URL '/' to the 'index' view
]