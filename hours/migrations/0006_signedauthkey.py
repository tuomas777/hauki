# Generated by Django 3.1.2 on 2020-11-20 08:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hours", "0005_signedauthentry"),
    ]

    operations = [
        migrations.CreateModel(
            name="SignedAuthKey",
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
                ("signing_key", models.TextField(verbose_name="Signing key")),
                ("valid_after", models.DateTimeField(verbose_name="Key valid after")),
                (
                    "valid_until",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Key valid until"
                    ),
                ),
                (
                    "data_source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.DJANGO_ORGHIERARCHY_DATASOURCE_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Signed auth key",
                "verbose_name_plural": "Signed auth keys",
            },
        ),
    ]
