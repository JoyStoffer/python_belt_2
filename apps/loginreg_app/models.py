from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, form_data):
        errors = []

        #Name
        if len(form_data['name']) < 2:
            errors.append("Name is required and must be at least 3 characters .")
        #Username
        if len(form_data['username']) < 2:
            errors.append("Username is required and must be at least 3 characters.")
        #Password
        if len(form_data['password']) < 7:
            errors.append("Password must be at least 8 characters.")
        #Password Confirmation
        if form_data['password'] != form_data['password_confirmation']:
            errors.append("Passwords must match.")

        return errors

    def create_user(self, form_data):
        hashedpw = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
        return User.objects.create(
            name = form_data['name'],
            username = form_data['username'],
            password = hashedpw,
        )

    def validate_login(self, form_data):
        errors = []
        #Email
        if len(form_data['username']) == 0:
            errors.append ("Username is required")
        #Password
        if len(form_data['password']) == 0:
            errors.append ("Password is required")

        user = User.objects.filter(username = form_data['username']).first()

        if user:
            user_password = form_data['password'].encode()
            db_password = user.password.encode()

            if bcrypt.checkpw(user_password, db_password):
                return {'user': user}

        errors.append("Username or password does not match.")
        return {'errors': errors}

    def current_user(self,request):
        return self.get(id = request.session['user_id'])


class User(models.Model):
    name = models.CharField(max_length = 45)
    username = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)

    objects = UserManager()

    def __str__(self):
        return "{} {} {} {}".format(self.id, self.name, self.username, self.password)
