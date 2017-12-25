# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-17 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnersDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('din', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Dinners')),
            ],
        ),
    ]
