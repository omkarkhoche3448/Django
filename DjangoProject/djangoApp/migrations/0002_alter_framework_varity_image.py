# Generated by Django 5.1 on 2024-09-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framework_varity',
            name='image',
            field=models.ImageField(upload_to='djangoApp/images'),
        ),
    ]
