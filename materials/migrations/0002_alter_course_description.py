# Generated by Django 5.1.3 on 2024-11-14 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Describe the course",
                max_length=500,
                null=True,
                verbose_name="Description",
            ),
        ),
    ]