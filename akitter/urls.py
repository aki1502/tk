from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views



urlpatterns = [
    path("", views.GlobalTimeLine.as_view(), name="global_timeline"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", LoginView.as_view(template_name="registration/signin.html"), name="signin"),
    path("signout/", LogoutView.as_view(next_page="global_timeline"), name="signout"),
    path("howtouse/", views.how_to_use, name="how_to_use_akitter")
]
