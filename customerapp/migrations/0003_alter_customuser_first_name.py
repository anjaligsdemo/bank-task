# Generated by Django 4.2.3 on 2023-07-07 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customerapp", "0002_district_wikipedia_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(max_length=150),
        ),
    ]