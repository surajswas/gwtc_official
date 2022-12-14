# Generated by Django 4.1.4 on 2022-12-14 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("fullname", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.CharField(max_length=255)),
                ("msg_date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
