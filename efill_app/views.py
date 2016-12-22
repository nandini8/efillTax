from django.shortcuts import render
from efill_app.forms import PersonalInfoForm
from django.http import HttpResponse
from efill_app.models import PersonalInfo
from django.core.exceptions import ValidationError
from django.db import IntegrityError, DataError
import re
# Create your views here.


def itr_form_view(request):
	error = None
	if request.method == 'POST':
		try:
			perosnal_obj = PersonalInfo.objects.create(pan_number=request.POST['pan_number'], last_name=request.POST['last_name'])
			if re.match(r'^[A-Z]{5}[0-9A-Z]{5}$',perosnal_obj.pan_number ) and len(perosnal_obj.pan_number) == 10:
				perosnal_obj.full_clean()
			else:
				perosnal_obj.delete()
				error = "Invalid PAN number"
		except IntegrityError:
			error = "Pan number should be unique"
		except DataError as e:
			error = "Invalid PAN number"
		except ValidationError:
			error = "Last name cannot be empty"

	return render(request, 'ITRform.html',{'error': error})


