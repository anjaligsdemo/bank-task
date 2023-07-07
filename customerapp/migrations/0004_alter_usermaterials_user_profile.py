# Generated by Django 4.2.3 on 2023-07-07 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("customerapp", "0003_alter_customuser_first_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermaterials",
            name="user_profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_materials",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
