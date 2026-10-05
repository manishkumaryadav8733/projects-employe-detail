from django.contrib import admin
from .models import ChangeRequest
@admin.register(ChangeRequest)
class ChangeRequestAdmin(admin.ModelAdmin):
    list_display=('title','client','priority','status','assigned_to','created_at')
    list_filter=('priority','status','category')
