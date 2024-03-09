# Generated by Django 4.2.5 on 2024-02-22 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle_database', '0007_userdatatablestatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='datatable',
            name='full_id',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]