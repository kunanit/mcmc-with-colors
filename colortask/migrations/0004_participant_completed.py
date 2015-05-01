# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colortask', '0003_auto_20150501_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
