# Generated by Django 4.2.7 on 2023-12-04 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0034_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
    ]
