from .models import Profile,Project
from django.forms import ModelForm
from django import forms

class PostProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('image',
                   'project_name',
                   'description',
                   'category',
                   'location',
                   'url',
        )