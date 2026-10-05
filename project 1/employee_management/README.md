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
