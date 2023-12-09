from django.contrib import admin
from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ('day', 'value', 'month')
    search_fields = ('day', 'value', 'month')
    list_filter = ('month',)


admin.site.register(Data, DataAdmin)

# Register your models here.
