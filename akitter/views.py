from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Prefetch, Q
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Akeet, Following, UserInfo
from .forms import AkeetForm, UserInfoForm



if False:
    Akeet.objects = None
    Following.objects = None
    UserInfo.objects = None
    UserInfo.DoesNotExist = None


class GlobalTimeLine(View):
    def get(self, request, *args, **kwargs):
        d = {
            "akeet_form": AkeetForm()
        }
        return render(request, "akitter/GTL.html", d)

    def post(self, request, *args, **kwargs):
        d = {
            "akeet_form": AkeetForm(request.POST),
        }
        if d["akeet_form"].is_valid():
            if request.user.is_authenticated:
                akeet = d["akeet_form"].save(commit=False)
                akeet.author = request.user
                akeet.published_date = timezone.now()
                akeet.save()
                return redirect("global_timeline")
        return render(request, "akitter/GTL.html", d)


class TimeLineFrameView(View):
    def get(self, request, *args, **kwargs):
        d = {
            "akeets": Akeet.objects.all().order_by("-published_date")[:100],
        }
        return render(request, "akitter/timeline_frame.html", d)


class PhoneTimeLineFrameView(View):
    def get(self, request, *args, **kwargs):
        d = {
            "akeets": Akeet.objects.all().order_by("-published_date")[:100],
        }
        return render(request, "akitter/phone_timeline_frame.html", d)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = "global_timeline"

    def form_valid(self, form):
        user = form.save()
        UserInfo.objects.create(user=user, origin="images/userimages/default_image.png")
        login(self.request, user)
        self.object = user
        return redirect(self.success_url)


class UserDetailView(DetailView):
    model = User
    template_name = "akitter/user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["akeets"] = Akeet.objects.filter(author=context["user"]).order_by("-published_date")[:100]
        context["following"] = not isinstance(self.request.user, AnonymousUser) \
                               and Following.objects.filter(follower=self.request.user, followee=context["user"]).exists()
        return context


class FollowView(RedirectView):
    url = "user_detail"

    def get(self, request, pk, *args, **kwargs):
        followee = get_object_or_404(User, pk=pk)
        d = {
            "follower": request.user,
            "followee": followee,
        }
        if d["follower"] != d["followee"]:
            following = Following.objects.filter(**d)
            if following.exists():
                following.delete()
            else:
                Following.objects.create(**d)
        return redirect(self.url, pk=pk)


class EditProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        if request.user != user:
            return redirect("user_detail", pk=pk)
        try :
            userinfo = UserInfo.objects.get(user=user)
        except UserInfo.DoesNotExist:
            userinfo = UserInfo.objects.create(user=user, origin="images/userimages/default_image.png")
        d = {
            "userinfo_form": UserInfoForm(instance=userinfo)
        }
        return render(request, "akitter/user_detail_edit.html", d)

    def post(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        userinfo = get_object_or_404(UserInfo, user=user)
        d = {
            "userinfo_form": UserInfoForm(request.POST, instance=userinfo),
        }
        if d["userinfo_form"].is_valid():
            userinfo = d["userinfo_form"].save(commit=False)
            userinfo.origin = request.FILES["origin"]
            userinfo.save()
            return redirect("user_detail", pk=pk)
        return render(request, "akitter/user_detail_edit.html", d)


class TimeLineView(View):
    def get(self, request, pk, *args, **kwargs):
        d = {
            "akeet_form": AkeetForm(),
            "pk": pk,
        }
        return render(request, "akitter/TL.html", d)

    def post(self, request, pk, *args, **kwargs):
        d = {
            "akeet_form": AkeetForm(request.POST),
            "pk": pk,
        }
        if d["akeet_form"].is_valid():
            if request.user.is_authenticated:
                akeet = d["akeet_form"].save(commit=False)
                akeet.author = request.user
                akeet.published_date = timezone.now()
                akeet.save()
                return redirect("local_timeline")
        return render(request, "akitter/TL.html", d)


class LocalTimeLineFrameView(View):
    def get(self, request, pk, *args, **kwargs):
        queryset = Following.objects.select_related("follower").filter(follower__pk=pk)
        prefetch = Prefetch("followed", queryset=queryset)
        authors = User.objects.prefetch_related(prefetch).filter(Q(followed__in=queryset) | Q(pk=pk))
        d = {
            "akeets": Akeet.objects.select_related("author").filter(author__in=authors).order_by("-published_date")[:100],
        }
        return render(request, "akitter/timeline_frame.html", d)


class PhoneLocalTimeLineFrameView(View):
    def get(self, request, pk, *args, **kwargs):
        queryset = Following.objects.select_related("follower").filter(follower__pk=pk)
        prefetch = Prefetch("followed", queryset=queryset)
        authors = User.objects.prefetch_related(prefetch).filter(Q(followed__in=queryset) | Q(pk=pk))
        d = {
            "akeets": Akeet.objects.select_related("author").filter(author__in=authors).order_by("-published_date")[:100],
        }
        return render(request, "akitter/phone_timeline_frame.html", d)
