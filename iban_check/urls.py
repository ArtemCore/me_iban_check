from django.urls import path

from iban_check import views

urlpatterns = [
    path("", views.main, name="main"),
    path("check", views.validate_iban, name="validate"),
]