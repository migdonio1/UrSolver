# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('skill', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Solvers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('solverUsername', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('fechaRegistro', models.DateTimeField(verbose_name='fecha de creacion')),
                ('solverEmail', models.EmailField(max_length=70)),
                ('solverName', models.CharField(max_length=200)),
                ('solverAge', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='skill',
            name='username',
            field=models.ForeignKey(to='polls.Solvers'),
        ),
    ]
