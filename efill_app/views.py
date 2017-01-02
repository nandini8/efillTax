from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from efill_app.forms import PersonalInfoForm
from django.http import HttpResponse
from efill_app.models import PersonalInfo
from django.core.exceptions import ValidationError
from django.db import IntegrityError, DataError
import re
# Create your views here.



def login(request):
	if request.user.is_authenticated():
		logout(request)
	return render(request, 'login.html')

@login_required(login_url='/')
def itr_form_view(request):
	error = None
	if request.method == 'POST':
		error = test_all(request)

	return render(request, 'ITRform.html',{'error': error})

def logout(request):
    auth_logout(request)
    return redirect('/')


def test_all(request):
	error = {}
	error['pan'] = validate_pan_number(request)
	error['last_name'] = validate_last_name(request)
	error['first_name'] = validate_first_name(request)
	error['middle_name'] = validate_middle_name(request)
	return error

def validate_pan_number(request):
	error = None
	pan_number = request.POST['pan_number']
	if not re.match(r'^[A-Z]{5}[0-9A-Z]{5}$',pan_number):
		error = "Invalid PAN number"
		return error
	#else: #PersonalInfo.objects.filter(pan_number = pan_number):
		#return error
	return error

def validate_last_name(request):
	error = None
	last_name = request.POST['last_name']
	if not re.match(r'^[A-Za-z]{1,25}$', last_name):
		error = "Enter a valid last name"
		return error
	else:
		return error

def validate_first_name(request):
	error = None
	first_name = request.POST['first_name']
	if re.match(r'^[A-Za-z]{1,25}$', first_name) or first_name == "":
		return error
	else:
		error = "Enter a valid first name"
		return error

def validate_middle_name(request):
	error = None
	middle_name = request.POST['middle_name']
	if re.match(r'^[A-Za-z]{1,25}$', middle_name) or middle_name == "":
		return error
	else:
		error = "Enter a valid middle name"
		return error

	