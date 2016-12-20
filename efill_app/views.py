from django.shortcuts import render
from efill_app.forms import PersonalInfoForm
from django.http import HttpResponse

# Create your views here.


def itr_form_view(request):
	if request.method == 'POST':
	        return HttpResponse(request.POST['pan_number'])
	return render(request, 'ITRform.html')
