# Generated by Django 3.1.2 on 2020-11-27 12:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hours", "0009_merge_20201126_1559"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalresource",
            name="ancestry_data_source",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="historicalresource",
            name="ancestry_is_public",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="historicalresource",
            name="ancestry_organization",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="resource",
            name="ancestry_data_source",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="resource",
            name="ancestry_is_public",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="resource",
            name="ancestry_organization",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                null=True,
                size=None,
            ),
        ),
    ]
