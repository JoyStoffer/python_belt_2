
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from ..loginreg_app.models import User


# Create your models here.


class WishManager(models.Manager):
    def validate(self, form_data):
        errors = []
        #Item
        if len(form_data['item']) < 3:
            errors.append("You have things you want...add something!")

        return errors


    def create_wish(self, form_data, user):
        return self.create(
            item = form_data['item'],
            user = user,

        )



class Wish(models.Model):
    item = models.CharField(max_length = 255)
    wisher = models.ManyToManyField(User, related_name ='items')
    user = models.ForeignKey(User,related_name = 'wishes')
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)
    objects = WishManager()
