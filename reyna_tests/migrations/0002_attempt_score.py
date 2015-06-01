# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('reyna_tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='score',
            field=models.DecimalField(max_digits=5, default=Decimal('0'), decimal_places=2),
        ),
    ]
