from django.contrib import admin
from .models import EmployeeMetric
@admin.register(EmployeeMetric)
class EmployeeMetricAdmin(admin.ModelAdmin):
    list_display=('employee','projects_count','tasks_completed','coding_errors','overtime_hours','leave_days','client_feedback_score','team_help_points')
