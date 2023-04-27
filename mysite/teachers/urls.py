from django.urls import path

from . import views

urlpatterns = [
    path("", views.generate_teachers),
    path("list/", views.teachers_list_view),
]
