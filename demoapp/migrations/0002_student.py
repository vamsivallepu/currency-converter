# Generated by Django 5.0.6 on 2024-07-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("age", models.IntegerField()),
                ("standard", models.IntegerField()),
            ],
        ),
    ]
