# Generated by Django 5.0.2 on 2024-02-12 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle_database', '0003_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]