# Generated by Django 5.0 on 2023-12-14 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0050_rename_co_attendance_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='co',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='finalapp.course'),
            preserve_default=False,
        ),
    ]
