from django.contrib import admin
from financial.models import Shares, UserShares


# Register your models here.
class UserSharesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'share']


class SharesAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'company', 'price']


admin.site.register(Shares, SharesAdmin)
admin.site.register(UserShares, UserSharesAdmin)
