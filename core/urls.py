from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('mvt-tile/<int:zoom>/<int:x>/<int:y>', views.mvt_tiles, name='mvt_tiles'),
]