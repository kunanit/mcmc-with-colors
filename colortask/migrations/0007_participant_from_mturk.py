# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colortask', '0006_color_parameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='from_mturk',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
