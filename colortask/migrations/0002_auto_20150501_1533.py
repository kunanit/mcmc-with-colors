# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colortask', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='color_left',
            field=models.CharField(max_length=16),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='color_right',
            field=models.CharField(max_length=16),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='selected_color',
            field=models.CharField(max_length=16),
            preserve_default=True,
        ),
    ]
