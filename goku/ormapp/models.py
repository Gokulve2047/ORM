from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
     loan_no=models.CharField(max_length=15,primary_key=True)
     name=models.CharField(max_length=100)
     age=models.IntegerField()
     interest=models.IntegerField()
     email=models.EmailField()

class BankloanAdmin(admin.ModelAdmin):
 list_display=("loan_no","name","age","interest","email")





