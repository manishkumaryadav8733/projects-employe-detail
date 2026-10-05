from django.urls import path
from .views import ai_dashboard, analyze_feedback_api, create_change_request
urlpatterns=[path('',ai_dashboard,name='ai_dashboard'),path('feedback/analyze/',analyze_feedback_api,name='ai_feedback_analyze'),path('change-request/create/',create_change_request,name='create_change_request')]
