# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colortask', '0004_participant_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='proposal_sd',
            field=models.FloatField(default=50),
            preserve_default=False,
        ),
    ]
