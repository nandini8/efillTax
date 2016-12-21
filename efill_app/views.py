from django.shortcuts import render
from efill_app.forms import PersonalInfoForm
from django.http import HttpResponse
from efill_app.models import PersonalInfo
from django.core.exceptions import ValidationError

# Create your views here.


def itr_form_view(request):
	error = None
	if request.method == 'POST':
		perosnal_obj = PersonalInfo.objects.create(pan_number=request.POST['pan_number'])
		try:
			perosnal_obj.full_clean()
		except ValidationError:
			perosnal_obj.delete()
			error = "Pan number cannot be empty."
	return render(request, 'ITRform.html',{'error': error})
