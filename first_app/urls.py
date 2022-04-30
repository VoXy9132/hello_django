from django.urls import path
from . import views

urlpatterns = [
    path('first_url', views.first_view),
    path('html_url', views.index)
]