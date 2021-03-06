# Generated by Django 2.2 on 2019-11-13 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0011_delete_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Hand'),
        ),
        migrations.AddField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(default=webapp.models.get_admin, on_delete=django.db.models.deletion.PROTECT, related_name='created_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
    ]
