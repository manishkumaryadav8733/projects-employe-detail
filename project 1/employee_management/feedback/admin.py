from django.contrib import admin
from .models import ClientFeedback
@admin.register(ClientFeedback)
class ClientFeedbackAdmin(admin.ModelAdmin):
    list_display = ('client','project_name','category','priority','created_at')
    list_filter = ('category','priority')
