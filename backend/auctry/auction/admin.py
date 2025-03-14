from django.contrib import admin
from .models import Items, auctons, Bids

# Register your models here.
admin.site.register(Items)
admin.site.register(Bids)
admin.site.register(auctons)
