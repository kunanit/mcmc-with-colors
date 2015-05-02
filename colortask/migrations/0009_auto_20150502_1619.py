# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colortask', '0008_participant_mturk_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='mturk_code',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
    ]
