# Generated by Django 2.1.5 on 2019-02-12 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190212_1334'),
        ('planner', '0002_auto_20190212_1334'),
        ('cases', '0003_auto_20190212_1334'),
        ('opportunity', '0003_auto_20190212_1334'),
        ('leads', '0004_auto_20190212_1334'),
        ('accounts', '0005_auto_20190212_1334'),
        ('common', '0006_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
        migrations.AlterField(
            model_name='attachments',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attachment_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='document',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='document_uploaded', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
