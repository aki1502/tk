from django import forms

from .models import Akeet, UserInfo



class AkeetForm(forms.ModelForm):

    class Meta:
        model = Akeet
        fields = ("text",)


class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ("origin", "vio",)
