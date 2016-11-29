from django.conf.urls import url
from . import views

#adding home URL
urlpatterns = [
    url(r'^$', views.home, name='home'),
]