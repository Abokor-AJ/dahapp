# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dahapp', '0003_auto_20171216_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='created_by',
        ),
        migrations.AlterModelOptions(
            name='cheque',
            options={'get_latest_by': 'created_on'},
        ),
        migrations.AlterModelOptions(
            name='deposit',
            options={'get_latest_by': 'created_on'},
        ),
        migrations.AlterModelOptions(
            name='loan',
            options={'get_latest_by': 'created_on'},
        ),
        migrations.AlterModelOptions(
            name='openingbalance',
            options={'get_latest_by': 'created_on'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'get_latest_by': 'created_on'},
        ),
        migrations.AlterModelOptions(
            name='refund',
            options={'get_latest_by': 'created_on'},
        ),
        migrations.AlterModelOptions(
            name='remittance',
            options={'get_latest_by': 'created_on'},
        ),
        migrations.AlterModelOptions(
            name='stamp',
            options={'get_latest_by': 'created_on'},
        ),
        migrations.AlterModelOptions(
            name='transfer',
            options={'get_latest_by': 'created_on'},
        ),
        migrations.AlterModelOptions(
            name='vouchers',
            options={'get_latest_by': 'created_on'},
        ),
        migrations.AlterModelOptions(
            name='withdrawal',
            options={'get_latest_by': 'created_on'},
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
    ]
