from django.db import models


class Task(models.Model):
    brief = models.CharField(max_length=100, null=False, blank=False, verbose_name='Brief description')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')
    status = models.ForeignKey('Status', related_name='tasks', on_delete=models.PROTECT)
    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    project = models.ForeignKey('Project', null=True, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')


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
