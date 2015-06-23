# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150622_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='value',
            field=models.CharField(max_length=256),
        ),
    ]
