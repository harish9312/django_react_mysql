# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length = 30, primary_key=True)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30, primary_key=True)
    phoneNo = models.CharField(max_length = 30)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.userName