# Generated by Django 5.1 on 2024-08-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookshelf", "0002_alter_customuser_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("publication_year", models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name="customuser",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
    ]
