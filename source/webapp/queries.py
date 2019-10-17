<<<<<<< HEAD
from webapp.models import Task, Status, Project, Type
from django.db.models import Q
from datetime import datetime, timedelta

query1 = Task.objects.filter(Q(status__name__iexact='done') & Q(updated_at__range=[(datetime.now() - timedelta(days=30)),datetime.now()]))
=======
from datetime import date, timedelta
from django.db.models import Q
from webapp.models import Project, Task, Type


query2 = Type.objects.filter(task__project=Project.objects.get(project_name='Tracker'))
query3 = Project.objects.filter(tasks__description__icontains='test')
>>>>>>> 465b0229739d3e88d7ca8bc469fd0c80f46c4548
