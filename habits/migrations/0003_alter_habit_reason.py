# Generated by Django 4.0.3 on 2022-03-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_remove_habit_milestone_milestone_date_finished_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='reason',
            field=models.TextField(blank=True),
        ),
    ]
