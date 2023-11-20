from django.urls import path

from .views import SubmoduleView

urlpatterns = [
    path("submodule/", SubmoduleView, name='remote submodule')
]