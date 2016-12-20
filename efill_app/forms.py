from django import forms
from efill_app.models import PersonalInfo

class PersonalInfoForm(forms.models.ModelForm):
	class Meta:
		model = PersonalInfo
		fields = ('pan_number', )
		widgets = {
			'text': forms.fields.TextInput(attrs={
			'placeholder': 'Enter a to-do item',
			'class': 'form-control input-lg',
			}),
		}