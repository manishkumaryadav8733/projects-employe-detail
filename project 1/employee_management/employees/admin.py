from django.contrib import admin
from .models import EmployeeProfile

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "user", "department", "designation", "manager", "annual_paid_leave", "is_active_employee")
    list_filter = ("department", "designation", "is_active_employee")
    search_fields = ("employee_id", "user__username", "user__first_name", "user__last_name")
