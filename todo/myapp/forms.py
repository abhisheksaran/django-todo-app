from django import forms
from .models import Todo


class todoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ['task','deadline', 'status']