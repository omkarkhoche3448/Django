# Generated by Django 5.1 on 2024-09-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0002_alter_framework_varity_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='framework_varity',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
