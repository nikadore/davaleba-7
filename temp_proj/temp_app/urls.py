from django.urls import path
from . import views

app_name = "temp_app"

urlpatterns = [
    path("", views.info_view, name="info"),
    path("hobbies/", views.hobbies_view, name="hobbies"),
]
