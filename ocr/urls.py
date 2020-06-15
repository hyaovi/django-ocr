from django.urls import include, path

from . import views

urlpatterns = [
    path('', view=views.homepage, name='homepage'),
]
