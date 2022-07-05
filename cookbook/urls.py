from django.urls import path
from .views import recipes_view

app_name = 'cookbbok'

urlpatterns = [
    path('', recipes_view),
]


