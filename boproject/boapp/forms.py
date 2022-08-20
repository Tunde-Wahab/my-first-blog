from django import forms

from boapp.models import Dupee

class PostForm(forms.ModelForm):

    class Meta:
        model = Dupee
        fields = ('name')
