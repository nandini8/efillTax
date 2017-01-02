# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('pan_number', models.CharField(primary_key=True, max_length=10, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=25)),
                ('middle_name', models.CharField(blank=True, max_length=25)),
                ('last_name', models.CharField(default='', max_length=25)),
                ('flat_no', models.CharField(default=' ', max_length=5)),
                ('premise_name', models.CharField(blank=True, max_length=15)),
                ('road_name', models.CharField(blank=True, max_length=10)),
                ('area_name', models.CharField(default=' ', max_length=15)),
                ('city_name', models.CharField(default=' ', max_length=15)),
                ('state_name', models.CharField(default=' ', max_length=20)),
                ('country_name', models.CharField(default=' ', max_length=20)),
                ('pincode', models.CharField(default=' ', max_length=6)),
                ('martial_status', models.CharField(default='Unmarried', max_length=10)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('sex', models.CharField(default='Male', max_length=6)),
                ('email_id', models.CharField(default=' ', max_length=25)),
                ('mobile_1', models.CharField(default=' ', max_length=10)),
                ('mobile_2', models.CharField(blank=True, max_length=10)),
                ('std_code', models.CharField(blank=True, max_length=5)),
                ('phone_no', models.CharField(blank=True, max_length=8)),
                ('employer_category', models.CharField(default='OTH', max_length=3)),
            ],
        ),
    ]
