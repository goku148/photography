# Generated by Django 5.1.3 on 2025-01-15 18:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='work_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='work_completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
