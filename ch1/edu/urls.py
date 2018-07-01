from django.conf.urls import url
from .views import _main



urlpatterns = [
    url(r'^$', _main, name='_main'),
]