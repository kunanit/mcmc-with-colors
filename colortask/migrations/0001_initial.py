# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('target_color', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_number', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('color_left', models.CharField(max_length=7)),
                ('color_right', models.CharField(max_length=7)),
                ('selected_color', models.CharField(max_length=7)),
                ('participant', models.ForeignKey(to='colortask.Participant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
