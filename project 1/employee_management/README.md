# Employee Management System

Django foundation for:
- Employee authentication and roles
- Employee profiles
- Attendance
- Paid leaves
- Overtime
- Progress and performance
- Rewards
- Projects
- Meetings
- Office activities
- Suggestions and new project ideas

## Setup

```bash
py -3.14 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Login: http://127.0.0.1:8000/login/
- Dashboard: http://127.0.0.1:8000/dashboard/
- Admin: http://127.0.0.1:8000/admin/

## AI Integration

This version adds `ai_analytics`, `clients`, `feedback`, `change_requests`, and `messaging` apps.

1. Create a virtual environment.
2. Run `pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and add your OpenAI API key if you want LLM analysis.
4. Run `python manage.py makemigrations`.
5. Run `python manage.py migrate`.
6. Run `python manage.py createsuperuser` if needed.
7. Run `python manage.py runserver`.
8. Open `/ai/` after login.

Without an API key, employee scoring and basic feedback classification use a local fallback so the site can be tested without an AI service.

Do not commit `.env` or API keys to GitHub.
