# Generated by Django 5.1.3 on 2024-11-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiterform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='linkedin_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
