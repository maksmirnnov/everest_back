from django.contrib import admin
from .models import Seminar, Lector, SeminarPriceItem, SeminarPriceItemFuture, SeminarProgram, SeminarRegulation, \
    SeminarSphere


# admin.site.register(SeminarSphere)


class SeminarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


admin.site.register(Seminar, SeminarAdmin)


class SeminarProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'program_date', 'program', 'time_update', 'time_create')
    list_display_links = ('id', 'program', 'program_date')
    search_fields = ('program', 'program_date')
    list_filter = ('program', 'program_date', 'time_create')


admin.site.register(SeminarProgram, SeminarProgramAdmin)


class SeminarRegulationAdmin(admin.ModelAdmin):
    list_display = ('id', 'regulation_date', 'regulation', 'time_update', 'time_create')
    list_display_links = ('id', 'regulation', 'regulation_date')
    search_fields = ('regulation', 'regulation_date')
    list_filter = ('regulation', 'regulation_date', 'time_create')


admin.site.register(SeminarRegulation, SeminarRegulationAdmin)


class LectorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'is_published')
    list_display_links = ('username', 'first_name')
    search_fields = ('first_name', 'is_published')
    list_editable = ('is_published',)


admin.site.register(Lector, LectorAdmin)


class PriceItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    list_display_links = ('title',)
    search_fields = ('title', 'price')
    list_editable = ('price',)


admin.site.register(SeminarPriceItem, PriceItemAdmin)


class PriceItemFutureAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(SeminarPriceItemFuture, PriceItemFutureAdmin)


