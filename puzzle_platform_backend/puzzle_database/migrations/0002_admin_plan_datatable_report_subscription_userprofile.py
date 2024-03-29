# Generated by Django 5.0.2 on 2024-02-12 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle_database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=100)),
                ('admin_password', models.CharField(max_length=100)),
                ('admin_email', models.EmailField(max_length=254, unique=True)),
                ('login_status', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plan_type', models.CharField(max_length=100)),
                ('plan_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('task_no', models.IntegerField()),
                ('puzzle_no', models.IntegerField()),
                ('puzzle_name', models.CharField(max_length=255)),
                ('puzzle_video', models.URLField()),
                ('puzzle_question', models.TextField()),
                ('level', models.CharField(max_length=50)),
                ('puzzle_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puzzle_database.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('task_no', models.IntegerField()),
                ('puzzle_no', models.IntegerField()),
                ('question_view_status', models.BooleanField(default=False)),
                ('video_view_status', models.BooleanField(default=False)),
                ('puzzle_status', models.BooleanField(default=False)),
                ('task_status', models.BooleanField(default=False)),
                ('price_spend', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puzzle_database.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_plan_type', models.CharField(max_length=100)),
                ('sub_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sub_renewal', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puzzle_database.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_in_task', models.IntegerField()),
                ('user_in_puzzle', models.IntegerField()),
                ('question_status', models.BooleanField(default=False)),
                ('video_status', models.BooleanField(default=False)),
                ('wallet', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='puzzle_database.customuser')),
            ],
        ),
    ]
