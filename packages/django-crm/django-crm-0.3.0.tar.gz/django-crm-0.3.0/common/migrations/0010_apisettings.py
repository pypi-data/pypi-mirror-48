# Generated by Django 2.1.5 on 2019-02-13 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190212_1708'),
        ('common', '0009_document_shared_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='APISettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('apikey', models.CharField(default='a223998f39691c748515bca13519b7b3', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='settings_created_by', to=settings.AUTH_USER_MODEL)),
                ('lead_assigned_to', models.ManyToManyField(related_name='lead_assignee_users', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='accounts.Tags')),
            ],
        ),
    ]
