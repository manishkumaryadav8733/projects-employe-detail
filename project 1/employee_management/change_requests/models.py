from django.conf import settings
from django.db import models

class ChangeRequest(models.Model):
    class Status(models.TextChoices):
        NEW='NEW','New'; ASSIGNED='ASSIGNED','Assigned'; IN_PROGRESS='IN_PROGRESS','In Progress'; COMPLETED='COMPLETED','Completed'; REJECTED='REJECTED','Rejected'
    class Priority(models.TextChoices):
        LOW='LOW','Low'; MEDIUM='MEDIUM','Medium'; HIGH='HIGH','High'; URGENT='URGENT','Urgent'
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='change_requests')
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, blank=True)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.MEDIUM)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.NEW)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_change_requests')
    ai_summary = models.TextField(blank=True)
    ai_action = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.title
