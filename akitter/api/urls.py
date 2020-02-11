from django.urls import path, include

from . import views as api_views



urlpatterns = [
    path("akeets/", api_views.AkeetListCreateAPIView.as_view()),
    path("auth/", include("djoser.urls.authtoken")),
    path("register/", api_views.AccountCreateAPIView.as_view()),
]
