from django.contrib import admin
from loanapp.models import AuthUsers, LoanEntries, LoanEligibility

# Register your models here.
class AuthUserAdmin(admin.ModelAdmin):
    model = AuthUsers

    list_display = ["username", "emailid"]
    list_filter = ["username"]

class LoanEntriesAdmin(admin.ModelAdmin):
    model = LoanEntries

    list_display = ["cust_name", "loan_amount", "earn_amount", "year"]
    list_filter = ["cust_name", "year"]

class LoanStatus(admin.ModelAdmin):
    model = LoanEligibility

    list_display = ["customername", "loan_amount", "earn_amount", "loan_limit", "year"]
    list_filter = ["customername", "year", "loan_limit"]


admin.site.register(AuthUsers, AuthUserAdmin)
admin.site.register(LoanEntries, LoanEntriesAdmin)
admin.site.register(LoanEligibility, LoanStatus)

admin.site.site_title = "Loan Administration"
admin.site.site_header = "Loan Administration"
