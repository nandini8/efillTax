from django.test import TestCase
from django.http import HttpRequest
from efill_app.views import itr_form_view
from efill_app.models import PersonalInfo
from django.core.exceptions import ValidationError
from django.db import IntegrityError, DataError


# Create your tests here.

class HomePageView(TestCase):

	def test_home_page_template_rendered(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'ITRform.html')

	def test_can_save_POST_requests_in_object(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['pan_number'] = 'AAAPL1234C'

		response = itr_form_view(request)
		self.assertEqual('AAAPL1234C',PersonalInfo.objects.first().pan_number)