from django.test import TestCase
from django.http import HttpRequest
from efill_app.views import itr_form_view
from efill_app.models import PersonalInfo
from django.core.exceptions import ValidationError

# Create your tests here.

class HomePageView(TestCase):

	def test_home_page_template_rendered(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'ITRform.html')

	def test_can_save_POST_requests_in_object(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['pan_number'] = '1234567890'

		response = itr_form_view(request)
		self.assertEqual('1234567890',PersonalInfo.objects.first().pan_number)


class PersonalInfoModelTest(TestCase):

	def test_pan_cannot_be_empty(self):
		personal_obj = PersonalInfo.objects.create(pan_number='')
		with self.assertRaises(ValidationError):
			personal_obj.full_clean()

class PersonalInfoViewTest(TestCase):

	def test_validation_errors_are_sent_back(self):
		response = self.client.post('/', data={'pan_number': ''})
		expected_error = "Pan number cannot be empty."
		self.assertContains(response, expected_error)