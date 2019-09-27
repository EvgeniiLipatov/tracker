from django.db import models

class Task(models.Model):
    brief = models.CharField(max_length=100, null=False, blank=False, verbose_name='Brief description')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')
    status = models.ForeignKey('Status',on_delete=models.PROTECT)
    type = models.ForeignKey('Type',on_delete=models.PROTECT)
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

