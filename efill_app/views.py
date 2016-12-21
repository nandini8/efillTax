from django.shortcuts import render
from efill_app.forms import PersonalInfoForm
from django.http import HttpResponse
from efill_app.models import PersonalInfo
from django.core.exceptions import ValidationError
from django.db import IntegrityError
import re
# Create your views here.


def itr_form_view(request):
	error = None
	if request.method == 'POST':
		try:
			perosnal_obj = PersonalInfo.objects.create(pan_number=request.POST['pan_number'])
			if re.match(r'^[A-Z]{5}[0-9A-Z]{5}$',perosnal_obj.pan_number ):
				perosnal_obj.full_clean()
			else:
				perosnal_obj.delete()
				error = "Invalid PAN number"
		except IntegrityError:
			error = "Pan number should be unique"

	return render(request, 'ITRform.html',{'error': error})


