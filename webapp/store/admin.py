from django.contrib import admin

from . import models


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'formatted_cnpj',
        'formatted_phone',
        'city',
        'state',
    )

    list_filter = (
        'state',
    )

    search_fields = (
        'name',
        'phone_number',
        'cnpj',
    )
