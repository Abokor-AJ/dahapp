# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dahapp', '0002_auto_20171216_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheque',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
        migrations.AlterField(
            model_name='openingbalance',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
        migrations.AlterField(
            model_name='remittance',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
        migrations.AlterField(
            model_name='stamp',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='created_by',
            field=models.ForeignKey(to='dahapp.Profile'),
        ),
    ]
