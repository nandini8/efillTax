from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.

class PersonalInfo(models.Model):
	pan_number = models.CharField(max_length = 10, primary_key = True)
	first_name = models.CharField(max_length = 25, blank = True)
	middle_name = models.CharField(max_length = 25, blank = True)
	last_name = models.CharField(max_length = 25, default = "")
	flat_no = models.CharField(max_length = 5, default = " ")
	premise_name = models.CharField(max_length = 15, blank = True)
	road_name = models.CharField(max_length = 10, blank = True)
	area_name = models.CharField(max_length = 15, default = " ")
	city_name = models.CharField(max_length = 15, default = " ")
	state_name = models.CharField(max_length = 20, default = " ")
	country_name = models.CharField(max_length = 20, default = " ")
	pincode = models.CharField(max_length = 6, default = " ")
	martial_status = models.CharField(max_length = 10, default = "Unmarried")
	dob = models.DateField(default=date.today) 
	sex  = models.CharField(max_length = 6, default = "Male")
	email_id = models.CharField(max_length = 25, default = " ")
	mobile_1 = models.CharField(max_length = 10, default = " ")
	mobile_2 = models.CharField(max_length = 10, blank = True)
	std_code = models.CharField(max_length = 5, blank = True)
	phone_no = models.CharField(max_length = 8, blank = True)
	employer_category = models.CharField(max_length = 3, default = 'OTH')

	def __str__():
		return pan_number

