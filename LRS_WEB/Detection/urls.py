from django.urls import path
from . import views
app_name = 'Detection'
urlpatterns = [
    path('', views.detect, name = 'detectScene')
]