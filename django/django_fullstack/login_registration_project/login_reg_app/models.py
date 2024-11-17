import datetime
from django.db import models
import bcrypt
import re

class UserManger(models.Manager):

    def registration_validator(self, postData):
        errors = {}

        if len(postData['firstname']) < 2:
            errors['firstname'] = "The first name should be at least 2 character "

        if len(postData['lastname']) < 2:
            errors['lname'] = "The last name should be at least 2 character "

        if len(postData['birth_date']) > 0:
            releaseDate = datetime.datetime.strptime(
                postData['birth_date'], '%Y-%m-%d')
            todayDate = datetime.datetime.today()
            if todayDate < releaseDate:
                errors['birth_date'] = "Date should be in the past!"
        else:
            errors['birth_date'] = "Date of birth field is required!"
            
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):  
            errors['email'] = "Invalid email address!"
        else:
            try:
                email = User.objects.get(email__iexact=postData['email'])
                errors['email'] = "The email is taken please try another one"
            except:
                pass

        if len(postData['password']) < 8:
            errors['password'] = "password should be at least 8 characters"
        
        if postData['password'] != postData['confirmPW']:
            errors['confirmPW'] = "password is not equal to the confirm password"
        
        return errors
    
    def login_validator(self, postData):
        errors= {}
        user = User.objects.filter(email= postData['email'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']): 
            errors['login_email'] = "Email is not valid"
        user = User.objects.filter(email=postData['email'])
        if len(user) == 0 : 
            errors['login_email'] = "Email unused"
        else: 
            if not bcrypt.checkpw(postData['password'].encode(),user[0].password.encode()):
                errors['login'] = "Email or Password is incorrect !"
                
        return errors


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birth_date= models.DateTimeField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= UserManger()


