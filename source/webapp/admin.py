from django.contrib import admin

from webapp.models import Task, Type, Status

class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'brief', 'description', 'status','type','created_at']
    list_filter = ['status', 'type']
    list_display_links = ['pk', 'brief']
    search_fields = ['title', 'text']
    readonly_fields = ['created_at']

admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Type)

