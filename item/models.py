from django.db import models
from django.conf import settings
from django.shortcuts import render, redirect


class Item(models.Model):

    SKU             = models.IntegerField(unique=True, null = True)
    name            = models.CharField(max_length=250, unique = True)
    type            = models.CharField(max_length=250, default = 'raw' )
    unit_type       = models.CharField(max_length=10 )
    unit_price      = models.IntegerField()

    status          = models.IntegerField(default=1)
    created_at      = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    updated_at      = models.DateTimeField(verbose_name='date updated', auto_now_add=True)


    def __str__(self):

        return self.name
