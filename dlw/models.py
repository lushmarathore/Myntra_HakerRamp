# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver






class Userall(models.Model):
    userid=models.CharField(max_length=200,unique=True)
    pwd=models.CharField(max_length=20)
    email=models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)
    type_of_user=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    addr=models.CharField(max_length=100,null=True,blank=True)


class Items(models.Model):
    supp_id=models.CharField(max_length=20,null=True)
    item_id=models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=100,null=True)

    description=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True)
    quan=models.IntegerField(null=True)
    rate=models.IntegerField(null=True)
    color=models.CharField(max_length=100,null=True)
    size=models.CharField(max_length=5,null=True)
    pic=models.FileField(upload_to='Images/')
    status=models.CharField(max_length=10,null=True,default='0')

class Booking(models.Model):
    supp_id=models.CharField(max_length=20,null=True)
    cust_id=models.CharField(max_length=20,null=True)
    item_id=models.CharField(max_length=20,null=True)
    from_date=models.DateField(null=True)
    start_date=models.DateTimeField(null=True)
    book_date=models.DateField(null=True)
    end_date=models.DateTimeField(null=True)
    to_date=models.DateField(null=True)
    status=models.CharField(max_length=20,null=True,default="0")

class Feedback(models.Model):
    cust_id=models.CharField(max_length=20,null=True)
    feedback=models.CharField(max_length=100,null=True)
    