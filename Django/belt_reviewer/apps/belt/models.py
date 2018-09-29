from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be 2 characters minimum."
        if not postData['first_name'].isalpha():
            errors['first_name'] = "First name must be alphabetic."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be 2 characters minimum."
        if not postData['last_name'].isalpha():
            errors['last_name'] = "Last name must be alphabetic."
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['email']) == 0:
            errors['email'] = "Email cannot be blank."
        if not email_regex.match(postData['email']):
            errors['email'] = "Invalid email address."
        user = User.objects.filter(email = postData['email'])
        if len(user):
            errors['email'] = "Account already exists for this email."
        if postData['password'] != postData['confirm']:
            errors['password'] = "Passwords do not match."
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        return errors
    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])
        if len(user) == 0:
            errors['mail'] = "Could not be logged in."
        elif not bcrypt.checkpw(postData['password'].encode(), user[0].hash_pw.encode()):
            errors['pword'] = "Incorrect password."
        return errors

class PostManager(models.Manager):
    def post_validator(self, postData):
        errors = {}
        if 'message' in postData:
            if len(postData['message']) < 2:
                errors['message'] = "Text field must be at least 2 characters."
        elif 'comment' in postData:
            if len(postData['comment']) < 2:
                errors['comment'] = "Comment field must be at least 2 characters."
        return errors
     
class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    hash_pw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default = " ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="books")
    objects = PostManager()

class Review(models.Model):
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stars = models.IntegerField(default = 0)
    user = models.ForeignKey(User, related_name = "user_reviews")
    book = models.ForeignKey(Book, related_name = "book_reviews")
    objects = PostManager()