# Generated by Django 5.0 on 2023-12-12 06:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0046_attendance_present_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendance',
            name='Co',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='finalapp.student'),
        ),
    ]
