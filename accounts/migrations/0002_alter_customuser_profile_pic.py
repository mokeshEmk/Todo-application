# Generated by Django 4.1.5 on 2023-01-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_pic",
            field=models.ImageField(default="default.jpg", upload_to="profile_pic"),
        ),
    ]