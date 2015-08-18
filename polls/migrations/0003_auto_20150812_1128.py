# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150812_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solvers',
            old_name='solverAge',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='solvers',
            old_name='solverEmail',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='solvers',
            old_name='solverName',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='solvers',
            old_name='solverUsername',
            new_name='Username',
        ),
    ]
