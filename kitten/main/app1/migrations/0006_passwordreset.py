# Generated by Django 5.1.3 on 2025-01-07 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_booking_event_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=20)),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.camera_registration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.user_registration')),
            ],
        ),
    ]
