# Generated by Django 4.2.5 on 2023-11-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0003_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
