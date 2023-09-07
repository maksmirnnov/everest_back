from django.contrib import admin

from tickets.models import Ticket, EducationTicket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'org_name', 'email', 'phone_number', 'inn', 'kpp', 'bik', 'check_acc', 'corr_acc', 'time_create')
    list_display_links = ('id', 'org_name')
    search_fields = ('seminar', 'org_name', 'email', 'phone_number', 'inn', 'kpp', 'bik', 'check_acc', 'corr_acc')
    list_filter = ('seminar', 'org_name', 'time_create')


admin.site.register(Ticket, TicketAdmin)


class EducationTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'org_name', 'email', 'phone_number', 'message', 'time_create')
    list_display_links = ('id', 'org_name')
    search_fields = ('org_name', 'email', 'phone_number', 'message')
    list_filter = ('org_name', 'time_create')


admin.site.register(EducationTicket, EducationTicketAdmin)
