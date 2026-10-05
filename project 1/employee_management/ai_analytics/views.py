import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from employees.models import EmployeeProfile
from .models import EmployeeMetric
from .services import analyze_employee, analyze_feedback
from feedback.models import ClientFeedback
from change_requests.models import ChangeRequest

@login_required
def ai_dashboard(request):
    metrics=EmployeeMetric.objects.select_related('employee').all()
    ranked=[]
    for m in metrics:
        result=analyze_employee({'employee':m.employee.get_full_name() or m.employee.username,'projects_count':m.projects_count,'tasks_completed':m.tasks_completed,'coding_errors':m.coding_errors,'overtime_hours':float(m.overtime_hours),'leave_days':m.leave_days,'client_feedback_score':float(m.client_feedback_score),'team_help_points':m.team_help_points})
        score=result.get('score') if result.get('mode')=='local' else None
        ranked.append({'metric':m,'result':result,'score':score})
    ranked.sort(key=lambda x: x['score'] if x['score'] is not None else 0, reverse=True)
    return render(request,'ai_analytics/dashboard.html',{'ranked':ranked,'feedback_count':ClientFeedback.objects.count(),'change_count':ChangeRequest.objects.count()})

@login_required
def analyze_feedback_api(request):
    if request.method!='POST': return JsonResponse({'error':'POST required'},status=405)
    message=request.POST.get('message','').strip()
    if not message: return JsonResponse({'error':'message required'},status=400)
    result=analyze_feedback(message)
    return JsonResponse(result)

@login_required
def create_change_request(request):
    if request.method!='POST': return JsonResponse({'error':'POST required'},status=405)
    title=request.POST.get('title','').strip(); description=request.POST.get('description','').strip()
    if not title or not description: return JsonResponse({'error':'title and description required'},status=400)
    ai=analyze_feedback(description)
    category=ai.get('category','General Suggestion'); priority=ai.get('priority','MEDIUM')
    if priority not in dict(ChangeRequest.Priority.choices): priority='MEDIUM'
    cr=ChangeRequest.objects.create(client=request.user,title=title,description=description,category=category,priority=priority,ai_summary=ai.get('summary',''),ai_action=ai.get('developer_action',''))
    return JsonResponse({'id':cr.id,'category':category,'priority':priority,'status':cr.status,'message':'Change request sent to the development workflow.'})
