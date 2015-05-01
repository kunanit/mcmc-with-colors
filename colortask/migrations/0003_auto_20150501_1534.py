# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colortask', '0002_auto_20150501_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='color_left',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='color_right',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='selected_color',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
