# Generated by Django 4.2.7 on 2024-11-04 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_projects_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmers',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, upload_to='project_images/'),
        ),
    ]
