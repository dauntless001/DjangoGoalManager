from django import forms
from .models import Goal, Objective

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'duration']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'duration' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class ObjForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ['comment']
        widgets = {
            'comment' : forms.TextInput(attrs={'class': 'form-control'}),
        }