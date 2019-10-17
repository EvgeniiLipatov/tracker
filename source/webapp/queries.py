from datetime import date, timedelta
from django.db.models import Q
from webapp.models import Project, Task, Type


query2 = Type.objects.filter(task__project=Project.objects.get(project_name='Tracker'))
query3 = Project.objects.filter(tasks__description__icontains='test')