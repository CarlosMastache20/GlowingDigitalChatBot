# Generated by Django 4.1.5 on 2023-02-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_info_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="info",
            name="tEncargado",
            field=models.CharField(max_length=100, null=True),
        ),
    ]