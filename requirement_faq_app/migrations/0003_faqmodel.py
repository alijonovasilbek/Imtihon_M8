# Generated by Django 5.0.6 on 2024-05-16 19:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "requirement_faq_app",
            "0002_rename_part_text_en_requirementsmodel_req_text_en_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="FAQModel",
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
                ("faq_question_uz", models.CharField(max_length=255)),
                ("faq_question_en", models.CharField(max_length=255)),
                ("faq_answer_uz", ckeditor.fields.RichTextField()),
                ("faq_answer_en", ckeditor.fields.RichTextField()),
            ],
            options={
                "verbose_name": "FAQS",
                "db_table": "FAQ table",
                "ordering": ["-id"],
            },
        ),
    ]
