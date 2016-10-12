from django.db import models

# Create your models here.
class AuthUsers(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    emailid = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    class Meta:
        db_table = "registered_users"

class LoanEntries(models.Model):
    cust_name = models.CharField(max_length=50)
    loan_amount = models.CharField(max_length=50)
    earn_amount = models.IntegerField()
    loan_limit = models.IntegerField()
    check_email = models.EmailField(max_length=70, null=True, blank=True)
    year = models.CharField(max_length=4)
    class Meta:
        db_table = "loan_table"

class LoanEligibility(models.Model):
    customername = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    company = models.CharField(max_length=50)
    loan_amount = models.CharField(max_length=50)
    earn_amount = models.IntegerField()
    loan_limit = models.IntegerField()
    year = models.CharField(max_length=4)
    class Meta:
        db_table = "loan_eligibility"


