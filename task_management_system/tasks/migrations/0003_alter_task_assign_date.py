# Generated by Django 5.1 on 2024-09-24 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_category_alter_task_assign_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assign_date',
            field=models.DateField(),
        ),
    ]
