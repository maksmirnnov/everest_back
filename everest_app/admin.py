from django.contrib import admin
from .models import Seminar, Lector, SeminarPriceItem, SeminarSphere, SeminarFormat


admin.site.register(SeminarSphere)
admin.site.register(SeminarFormat)


class SeminarAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'time_create', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'date_start', 'time_create')
    readonly_fields = ('time_create', 'time_update')
    save_as = True
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Seminar, SeminarAdmin)


class LectorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'is_published')
    list_display_links = ('username', 'first_name')
    search_fields = ('first_name', 'is_published')
    list_editable = ('is_published',)
    save_as = True
    prepopulated_fields = {'username': ('last_name',)}


admin.site.register(Lector, LectorAdmin)


class PriceItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'seminar', 'price')
    list_display_links = ('title',)
    search_fields = ('title', 'seminar', 'price')
    list_editable = ('price',)
    save_as = True


admin.site.register(SeminarPriceItem, PriceItemAdmin)
