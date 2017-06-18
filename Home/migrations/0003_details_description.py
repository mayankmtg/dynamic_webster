# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20170618_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='description',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
