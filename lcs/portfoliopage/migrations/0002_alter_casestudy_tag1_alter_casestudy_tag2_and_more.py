# Generated by Django 5.1.3 on 2024-12-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudy',
            name='tag1',
            field=models.JSONField(max_length=50),
        ),
        migrations.AlterField(
            model_name='casestudy',
            name='tag2',
            field=models.JSONField(max_length=50),
        ),
        migrations.AlterField(
            model_name='casestudy',
            name='tag3',
            field=models.JSONField(max_length=50),
        ),
    ]
