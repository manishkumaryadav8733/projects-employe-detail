from django.conf import settings
from django.db import models

class EmployeeMetric(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ai_metrics')
    projects_count = models.PositiveIntegerField(default=0)
    tasks_completed = models.PositiveIntegerField(default=0)
    coding_errors = models.PositiveIntegerField(default=0)
    overtime_hours = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    leave_days = models.PositiveIntegerField(default=0)
    client_feedback_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    team_help_points = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return f'AI metrics: {self.employee}'
