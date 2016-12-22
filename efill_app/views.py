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
		error = test_all(request)

	return render(request, 'ITRform.html',{'error': error})


def test_all(request):
	error = {}
	error['pan'] = validate_pan_number(request)
	error['last_name'] = validate_last_name(request)
	return error

def validate_pan_number(request):
	error = None
	pan_number = request.POST['pan_number']
	if not re.match(r'^[A-Z]{5}[0-9A-Z]{5}$',pan_number) and not len(pan_number) == 10:
		error = "Invalid PAN number"
		return error
	else: #PersonalInfo.objects.filter(pan_number = pan_number):
		error = "Invalid PAN number"
		return error
	return error

def validate_last_name(request):
	error = None
	last_name = request.POST['last_name']
	if not re.match(r'^[A-Za-z]{1,25}$', last_name):
		error = "Last name should contain characters only"
		return error
	else:
		return error

	