from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import TemplateView

from . import views
from .api import views as api_views



urlpatterns = [
    path("", views.GlobalTimeLine.as_view(), name="global_timeline"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", LoginView.as_view(template_name="registration/signin.html"), name="signin"),
    path("signout/", LogoutView.as_view(next_page="global_timeline"), name="signout"),
    path("howtouse/", TemplateView.as_view(template_name="akitter/how_to_use.html"), name="how_to_use_akitter"),
    path("timeline_frame/", views.TimeLineFrameView.as_view(), name="timeline_frame"),
    path("phone_timeline_frame/", views.PhoneTimeLineFrameView.as_view(), name="phone_timeline_frame"),
    path("user/<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),
    path("user/<int:pk>/follow/", views.FollowView.as_view(), name="follow"),
    path("user/<int:pk>/edit/", views.EditProfileView.as_view(), name="edit_profile"),
    path("user/<int:pk>/timeline/", views.TimeLineView.as_view(), name="local_timeline"),
    path("user/<int:pk>/timeline_frame/", views.LocalTimeLineFrameView.as_view(), name="local_timeline_frame"),
    path("user/<int:pk>/phone_timeline_frame/", views.PhoneLocalTimeLineFrameView.as_view(), name="phone_local_timeline_frame"),
    path("api/akeets/", api_views.AkeetListAPIView.as_view()),
]
