# Generated by Django 2.1.7 on 2019-06-03 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0003_merge_20190214_1427'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Event')),
                ('event_type', models.CharField(choices=[('Recurring', 'Recurring'), ('Non-Recurring', 'Non-Recurring')], max_length=20)),
                ('status', models.CharField(blank=True, choices=[('Planned', 'Planned'), ('Held', 'Held'), ('Not Held', 'Not Held'), ('Not Started', 'Not Started'), ('Started', 'Started'), ('Completed', 'Completed'), ('Canceled', 'Canceled'), ('Deferred', 'Deferred')], max_length=64, null=True)),
                ('start_date', models.DateField(default=None)),
                ('start_time', models.TimeField(default=None)),
                ('end_date', models.DateField(default=None)),
                ('end_time', models.TimeField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('is_active', models.BooleanField(default=True)),
                ('disabled', models.BooleanField(default=False)),
                ('assigned_to', models.ManyToManyField(blank=True, related_name='event_assigned', to=settings.AUTH_USER_MODEL)),
                ('contacts', models.ManyToManyField(blank=True, related_name='event_contact', to='contacts.Contact')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_created_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
