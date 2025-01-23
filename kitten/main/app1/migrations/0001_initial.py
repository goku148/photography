# Generated by Django 5.1.3 on 2025-01-03 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('productprice', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='camera_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('experience', models.TextField()),
                ('qualifications', models.TextField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('is_accepted', models.CharField(default='pending', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('is_accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='available_Photographer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(null=True, upload_to='photographers/')),
                ('specialization', models.CharField(max_length=100)),
                ('rating', models.FloatField(default=0.0)),
                ('package', models.CharField(choices=[('CATEGORY', 'Category'), ('BASIC', 'basic'), ('PREMIUM', 'Premium')], default='CATEGORY', max_length=50)),
                ('availability', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('portfolio_link', models.URLField(max_length=500)),
                ('is_accepted', models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], default='PENDING', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.camera_registration')),
            ],
        ),
        migrations.CreateModel(
            name='PhotographerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photographer_images/')),
                ('category', models.CharField(max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app1.camera_registration')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.add_product')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('wedding', 'Wedding'), ('birthday', 'Birthday'), ('corporate', 'Corporate'), ('portrait', 'Portrait Session'), ('other', 'Other')], max_length=50)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_duration', models.PositiveIntegerField()),
                ('event_location', models.TextField()),
                ('requirements', models.TextField(blank=True, null=True)),
                ('package', models.CharField(choices=[('basic', 'Basic'), ('standard', 'Standard'), ('premium', 'Premium')], default='BASIC', max_length=50)),
                ('consent', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='app1.user_registration')),
            ],
        ),
    ]
