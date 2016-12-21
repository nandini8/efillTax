# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efill_app', '0002_auto_20161220_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='area_name',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='city_name',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='country_name',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='employer_category',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='flat_no',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='martial_status',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='mobile_1',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='mobile_2',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='premise_name',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='road_name',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='state_name',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='std_code',
        ),
    ]
