# Generated by Django 3.1.2 on 2021-01-04 10:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.DJANGO_ORGHIERARCHY_DATASOURCE_MODEL),
        ("users", "0002_auto_20201005_1851"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserOrigin",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "origin_id",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Origin ID"
                    ),
                ),
                (
                    "data_source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.DJANGO_ORGHIERARCHY_DATASOURCE_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="origins",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User origin",
                "verbose_name_plural": "User origins",
            },
        ),
        migrations.AddConstraint(
            model_name="userorigin",
            constraint=models.UniqueConstraint(
                fields=("data_source", "origin_id"),
                name="unique_user_origin_identifier_per_data_source",
            ),
        ),
    ]
