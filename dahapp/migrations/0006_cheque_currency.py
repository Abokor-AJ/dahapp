# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dahapp', '0005_auto_20180106_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheque',
            name='currency',
            field=models.CharField(default=b'USD', max_length=5),
        ),
    ]
