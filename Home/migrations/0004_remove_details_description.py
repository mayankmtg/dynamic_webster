# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_details_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='description',
        ),
    ]
