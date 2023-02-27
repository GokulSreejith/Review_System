from django import forms
from.models import Review

class reviewR (forms.ModelForm):
    class Meta:
        app_label = 'review'
        model = Review
        fields = ["name","email","review","rating","suggestion"]