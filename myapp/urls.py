from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.my_view, name='hello'),
]
