# Generated by Django 4.2.5 on 2024-03-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle_database', '0011_plan_benefits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdatatablestatus',
            name='status',
        ),
        migrations.AddField(
            model_name='userdatatablestatus',
            name='puzzle_status',
            field=models.CharField(choices=[('notstarted', 'notstarted'), ('incompleted', 'Incompleted'), ('completed', 'Completed')], default='notstarted', max_length=20),
        ),
        migrations.AddField(
            model_name='userdatatablestatus',
            name='task_status',
            field=models.CharField(choices=[('notstarted', 'notstarted'), ('incompleted', 'Incompleted'), ('completed', 'Completed')], default='notstarted', max_length=20),
        ),
        migrations.AddField(
            model_name='userdatatablestatus',
            name='time_spent',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
