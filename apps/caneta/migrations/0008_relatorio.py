# Generated by Django 4.1 on 2022-11-25 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("caneta", "0007_lote"),
    ]

    operations = [
        migrations.CreateModel(
            name="Relatorio",
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
                ("quantidade_falhas", models.IntegerField()),
                ("codigo", models.CharField(max_length=45)),
                (
                    "lote",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="caneta.lote"
                    ),
                ),
            ],
        ),
    ]
