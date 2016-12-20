# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('pan_number', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=25, blank=True)),
                ('middle_name', models.CharField(max_length=25, blank=True)),
                ('last_name', models.CharField(max_length=25)),
                ('flat_no', models.CharField(max_length=5)),
                ('premise_name', models.CharField(max_length=15, blank=True)),
                ('road_name', models.CharField(max_length=10, blank=True)),
                ('area_name', models.CharField(max_length=15)),
                ('district_name', models.CharField(max_length=15)),
                ('state_name', models.CharField(max_length=20)),
                ('country_name', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=6)),
                ('martial_status', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('sex', models.CharField(max_length=6)),
                ('email_id', models.CharField(max_length=25)),
                ('mobile_1', models.CharField(max_length=10)),
                ('mobile_2', models.CharField(max_length=10, blank=True)),
                ('std_code', models.CharField(max_length=5, blank=True)),
                ('phone_no', models.CharField(max_length=8, blank=True)),
                ('employer_category', models.CharField(max_length=3, default='OTH')),
            ],
        ),
    ]
