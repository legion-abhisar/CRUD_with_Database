# Generated by Django 4.2.6 on 2023-10-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(max_length=240),
        ),
    ]
