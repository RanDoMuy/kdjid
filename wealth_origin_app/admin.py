from django.contrib import admin
from .models import User, Deposit_History, Withdrawal_History
# Register your models here.

class UserProfile(admin.ModelAdmin):
    list_display = ("full_name", "verify", "profit_balance")

class UserDeposit(admin.ModelAdmin):
    list_display = ("user", "status", "amount")


admin.site.register(User, UserProfile)
admin.site.register(Deposit_History, UserDeposit)
admin.site.register(Withdrawal_History)