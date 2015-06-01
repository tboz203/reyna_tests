# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user', models.CharField(max_length=64)),
                ('date', models.DateTimeField()),
            ],
            options={
                'ordering': ('user', 'test', 'date'),
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=256)),
                ('is_correct', models.BooleanField()),
            ],
            options={
                'ordering': ('text',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('text',),
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(to='reyna_tests.Test'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='reyna_tests.Question'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='choices',
            field=models.ManyToManyField(to='reyna_tests.Choice'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='test',
            field=models.ForeignKey(to='reyna_tests.Test'),
        ),
    ]
