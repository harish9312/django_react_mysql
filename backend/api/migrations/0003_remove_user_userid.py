# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-23 11:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userId',
        ),
    ]
