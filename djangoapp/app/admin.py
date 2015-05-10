from django.contrib import admin
from models import *

class AppUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(AppUser, AppUserAdmin)

class OfferedServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(OfferedService, OfferedServiceAdmin)

class PurchasedServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(PurchasedService, PurchasedServiceAdmin)
