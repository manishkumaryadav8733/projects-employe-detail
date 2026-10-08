import os
import sys

path = "/home/yourusername/employee_management"
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "employee_management.settings"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


path = "/home/yourusername/employee_management"
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "employee_management.settings"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()