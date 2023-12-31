# Generated by Django 4.2.7 on 2023-12-02 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0020_remove_teacher_profile_remove_teacher_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherjob',
            old_name='email',
            new_name='enter_email',
        ),
        migrations.RenameField(
            model_name='teacherjob',
            old_name='phone_number',
            new_name='phone_num',
        ),
        migrations.RenameField(
            model_name='teacherjob',
            old_name='resume',
            new_name='upload_resume',
        ),
        migrations.RemoveField(
            model_name='teacherjob',
            name='cover_letter',
        ),
    ]
