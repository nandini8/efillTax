# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('efill_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='area_name',
            field=models.CharField(max_length=15, default=' '),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='city_name',
            field=models.CharField(max_length=15, default=' '),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='country_name',
            field=models.CharField(max_length=20, default=' '),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='email_id',
            field=models.CharField(max_length=25, default=' '),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='employer_category',
            field=models.CharField(max_length=3, default='OTH'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='flat_no',
            field=models.CharField(max_length=5, default=' '),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='martial_status',
            field=models.CharField(max_length=10, default='Unmarried'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='mobile_1',
            field=models.CharField(max_length=10, default=' '),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='mobile_2',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='phone_no',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='pincode',
            field=models.CharField(max_length=6, default=' '),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='premise_name',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='road_name',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='sex',
            field=models.CharField(max_length=6, default='Male'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='state_name',
            field=models.CharField(max_length=20, default=' '),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='std_code',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='last_name',
            field=models.CharField(max_length=25, default=''),
        ),
    ]
