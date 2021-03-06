from django.contrib.auth.models import User
from django.db import models


def get_admin():
    return User.objects.get(username='admin').id


class Task(models.Model):
    brief = models.CharField(max_length=100, null=False, blank=False, verbose_name='Brief description')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')
    status = models.ForeignKey('Status', on_delete=models.PROTECT)
    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    project = models.ForeignKey('Project', null=True, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update Time')
    created_by = models.ForeignKey(User, null=False, blank=False, default=get_admin, verbose_name='Author',
                                   on_delete=models.PROTECT, related_name='created_tasks')
    assigned_to = models.ForeignKey(User, null=True, blank=True, verbose_name='Hand', on_delete=models.PROTECT,
                                    related_name='assigned_tasks')


class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='Status')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "statuses"


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='Type')

    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(max_length=70, null=True, blank=True, verbose_name='Project name')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updating time')


    def __str__(self):
        return self.project_name
