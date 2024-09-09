# Generated by Django 5.1 on 2024-09-09 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0006_enrolledcourse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrolledcourse',
            old_name='enrolled_date',
            new_name='enrollment_date',
        ),
        migrations.AddField(
            model_name='framework_reviews',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoApp.framework_courses'),
        ),
    ]
