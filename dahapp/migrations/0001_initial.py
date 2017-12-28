# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cheque_no', models.CharField(max_length=15)),
                ('bank_name', models.CharField(max_length=70)),
                ('customer_name', models.CharField(max_length=50)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2)),
                ('description', models.CharField(max_length=100)),
                ('deposited_by', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2)),
                ('description', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2)),
                ('description', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=50)),
                ('authorized_by', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningBalance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usd', models.DecimalField(max_digits=10, decimal_places=2)),
                ('djf', models.DecimalField(max_digits=12, decimal_places=2)),
                ('receiver', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usd', models.DecimalField(max_digits=10, decimal_places=2)),
                ('djf', models.DecimalField(max_digits=12, decimal_places=2)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tt_no', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=50)),
                ('amount_full', models.DecimalField(max_digits=12, decimal_places=2)),
                ('amount_net', models.DecimalField(max_digits=12, decimal_places=2)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Remittance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usd', models.DecimalField(max_digits=10, decimal_places=2)),
                ('djf', models.DecimalField(max_digits=12, decimal_places=2)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Stamp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2)),
                ('description', models.CharField(max_length=100)),
                ('received_by', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vouchers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2)),
                ('description', models.CharField(max_length=100)),
                ('signed_by', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
                ('created_by', models.ForeignKey(to='dahapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2)),
                ('description', models.CharField(max_length=100)),
                ('withdrawn_by', models.CharField(max_length=50)),
                ('authorized_by', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(verbose_name=b'date created')),
                ('created_by', models.ForeignKey(to='dahapp.User')),
            ],
        ),
        migrations.AddField(
            model_name='transfer',
            name='created_by',
            field=models.ForeignKey(to='dahapp.User'),
        ),
        migrations.AddField(
            model_name='stamp',
            name='created_by',
            field=models.ForeignKey(to='dahapp.User'),
        ),
        migrations.AddField(
            model_name='remittance',
            name='created_by',
            field=models.ForeignKey(to='dahapp.User'),
        ),
        migrations.AddField(
            model_name='refund',
            name='created_by',
            field=models.ForeignKey(to='dahapp.User'),
        ),
        migrations.AddField(
            model_name='payment',
            name='created_by',
            field=models.ForeignKey(to='dahapp.User'),
        ),
        migrations.AddField(
            model_name='openingbalance',
            name='created_by',
            field=models.ForeignKey(to='dahapp.User'),
        ),
        migrations.AddField(
            model_name='loan',
            name='created_by',
            field=models.ForeignKey(to='dahapp.User'),
        ),
        migrations.AddField(
            model_name='expense',
            name='created_by',
            field=models.ForeignKey(to='dahapp.User'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='created_by',
            field=models.ForeignKey(to='dahapp.User'),
        ),
        migrations.AddField(
            model_name='cheque',
            name='created_by',
            field=models.ForeignKey(to='dahapp.User'),
        ),
    ]
