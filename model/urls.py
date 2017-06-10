from django.conf.urls import url
from model.views import create_container, create_image

urlpatterns = [
    url(r'^create/image/(?P<model>\w{0,50})', create_image, name='create_image'),
    url(r'^create', create_container, name='create_container'),
]