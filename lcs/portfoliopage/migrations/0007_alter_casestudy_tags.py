# Generated by Django 5.1.3 on 2024-12-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopage', '0006_jobapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudy',
            name='tags',
            field=models.JSONField(default=list),
        ),
    ]
