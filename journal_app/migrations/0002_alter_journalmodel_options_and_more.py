# Generated by Django 5.0.6 on 2024-05-16 17:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("journal_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="journalmodel",
            options={"ordering": ["-journal_date"], "verbose_name": "Journals"},
        ),
        migrations.AlterField(
            model_name="journalmodel",
            name="journal_desc_en",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="journalmodel",
            name="journal_desc_uz",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
