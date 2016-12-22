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
                ('pan_number', models.CharField(primary_key=True, max_length=10, serialize=False)),
                ('first_name', models.CharField(max_length=25, blank=True)),
                ('middle_name', models.CharField(max_length=25, blank=True)),
                ('last_name', models.CharField(max_length=25)),
            ],
        ),
    ]
