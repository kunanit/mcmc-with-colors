# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colortask', '0007_participant_from_mturk'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='mturk_code',
            field=models.BooleanField(default=b'', max_length=50),
            preserve_default=True,
        ),
    ]
