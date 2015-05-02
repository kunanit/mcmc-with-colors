# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colortask', '0009_auto_20150502_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='mturk_code',
            field=models.CharField(default=b'', max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='participant',
            name='proposal_sd',
            field=models.FloatField(verbose_name=b'proposal stdev'),
            preserve_default=True,
        ),
    ]
