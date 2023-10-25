from django import forms
from . models import candidate, skills, project

class cform(forms.ModelForm):
    class Meta:
        model = candidate
        fields = "__all__"

class pform(forms.ModelForm):
    class Meta:
        model = project
        fields = "__all__"

class sform(forms.ModelForm):
    class Meta:
        model = skills
        fields = "__all__"