from django.forms import ModelForm
from .models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','memo','important']


        widgets = {
            'title': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'memo': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),

                }
