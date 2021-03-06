# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('halfwayapp', '0007_auto_20160224_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='halfwayapp.Address'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='participant_two',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Participant_two', to='halfwayapp.Participant'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='trip_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='starting_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='halfwayapp.Address'),
        ),
    ]
