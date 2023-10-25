from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, blank=True)
    username = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    contact = models.BigIntegerField()
    occ = models.CharField(max_length=40)
    addr = models.CharField(max_length=255)
    password = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'candidate'

class project(models.Model):
    p_name = models.CharField(max_length=30)
    dur = models.IntegerField()
    tech = models.CharField(max_length=255)

    class Meta:
        db_table = 'project'

class skills(models.Model):
    s_name = models.CharField(max_length=50)
    level = models.CharField(max_length=15)

    class Meta:
        db_table = 'skills'

