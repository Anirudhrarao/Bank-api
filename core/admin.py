from django.contrib import admin
from core.models import Transactions,Category,Currency
# Register your models here.
admin.site.register(Transactions)
admin.site.register(Category)
admin.site.register(Currency)