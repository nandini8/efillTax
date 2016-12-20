# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efill_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalinfo',
            old_name='district_name',
            new_name='city_name',
        ),
    ]
