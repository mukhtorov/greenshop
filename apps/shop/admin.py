from django.contrib import admin
from .models import Plant, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {
        'slug': ('name',),
    }


class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', ]
    list_filter = ['name', 'price', 'available', ]
    list_editable = ['price', 'stock', 'available', ]
    prepopulated_fields = {
        'slug': ('name',),
    }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Plant, PlantAdmin)
