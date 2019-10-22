from django import forms

from .models import Akeet



class AkeetForm(forms.ModelForm):

    class Meta:
        model = Akeet
        fields = ("text",)


