from django import forms
from efill_app.models import PersonalInfo

class PersonalInfoForm(forms.models.ModelForm):
	class Meta:
		model = PersonalInfo
		fields = '__all__'