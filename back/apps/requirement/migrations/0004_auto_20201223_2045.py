# Generated by Django 3.1.4 on 2020-12-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("requirement", "0003_auto_20201223_2040"),
    ]

    operations = [
        migrations.AddField(
            model_name="requirement", name="text_en", field=models.TextField(null=True, verbose_name="Text"),
        ),
        migrations.AddField(
            model_name="requirement", name="text_ru", field=models.TextField(null=True, verbose_name="Text"),
        ),
        migrations.AddField(
            model_name="requirement",
            name="title_en",
            field=models.CharField(max_length=128, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="requirement",
            name="title_ru",
            field=models.CharField(max_length=128, null=True, verbose_name="Title"),
        ),
    ]