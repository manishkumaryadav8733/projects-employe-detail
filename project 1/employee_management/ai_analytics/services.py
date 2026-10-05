import json, os
from dotenv import load_dotenv
load_dotenv()

def _fallback_employee(data):
    score = 100
    score -= min(data.get('coding_errors',0)*4, 30)
    score += min(data.get('tasks_completed',0), 25)
    score += min(data.get('projects_count',0)*3, 15)
    score += min(data.get('team_help_points',0), 10)
    score -= min(float(data.get('leave_days',0))*0.5, 10)
    score = max(0, min(100, round(score, 1)))
    return {'mode':'local','score':score,'ranking_note':'Use as an operational metric, not an automatic employment decision.','summary':'AI API key not configured; local analytics used.','data':data}

def analyze_employee(data):
    api_key=os.getenv('OPENAI_API_KEY')
    if not api_key: return _fallback_employee(data)
    try:
        from openai import OpenAI
        client=OpenAI(api_key=api_key)
        prompt=f'''Analyze employee operational data for a management dashboard. Do not make decisions about hiring, firing, promotion or discipline. Identify workload, contribution, quality and risks transparently. Data: {json.dumps(data)} Return concise JSON with score (0-100), workload, strengths, attention_areas, summary.'''
        r=client.responses.create(model=os.getenv('OPENAI_MODEL','gpt-5-mini'), input=prompt)
        return {'mode':'ai','result':r.output_text}
    except Exception as e:
        return {'mode':'local','error':'AI service unavailable','fallback':_fallback_employee(data)}

def analyze_feedback(message):
    api_key=os.getenv('OPENAI_API_KEY')
    if not api_key:
        m=message.lower(); category='Feature Request' if any(x in m for x in ['add','need','want','option','feature']) else ('Bug' if any(x in m for x in ['error','bug','not working','issue']) else 'General Suggestion')
        return {'mode':'local','category':category,'priority':'MEDIUM','summary':message[:500],'developer_action':'Review the request and contact the client.'}
    try:
        from openai import OpenAI
        r=OpenAI(api_key=api_key).responses.create(model=os.getenv('OPENAI_MODEL','gpt-5-mini'), input=f'''Classify this client request. Return JSON with category (Bug, Feature Request, UI/UX, Performance, Complaint, Appreciation, General Suggestion), priority, related_module, summary, developer_action. Request: {message}''')
        return {'mode':'ai','result':r.output_text}
    except Exception:
        return {'mode':'local','category':'General Suggestion','priority':'MEDIUM','summary':message[:500],'developer_action':'Review the request manually.'}
