from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.utils import timezone

from .models import Akeet
from .forms import AkeetForm



if False:
    Akeet.objects = None

class GlobalTimeLine(View):
    def get(self, request, *args, **kwargs):
        d = {
            "akeets": Akeet.objects.all().order_by("-published_date")[:100],
            "akeet_form": AkeetForm()
        }
        return render(request, "akitter/GTL.html", d)

    def post(self, request, *args, **kwargs):
        d = {
            "akeets": Akeet.objects.all().order_by("-published_date")[:100],
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


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = "global_timeline"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return redirect(self.success_url)


def how_to_use(request):
    return render(request, "akitter/how_to_use.html")