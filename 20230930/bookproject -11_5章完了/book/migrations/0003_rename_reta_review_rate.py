# Generated by Django 4.2.5 on 2023-09-29 01:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0002_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="reta",
            new_name="rate",
        ),
    ]
