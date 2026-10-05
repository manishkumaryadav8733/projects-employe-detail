from django.conf import settings
from django.db import models

class ClientFeedback(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_feedback')
    project_name = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    category = models.CharField(max_length=50, blank=True)
    priority = models.CharField(max_length=20, blank=True)
    ai_summary = models.TextField(blank=True)
    developer_action = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.client} - {self.project_name or "General"}'
