# Generated by Django 4.1 on 2022-11-04 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fornecedor", "0001_initial"),
        ("caneta", "0006_alter_caneta_cor_alter_caneta_modelo_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lote",
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
                ("codigo_maquina", models.CharField(max_length=45)),
                ("data_fabricação", models.DateField()),
                ("quantidade", models.IntegerField()),
                (
                    "caneta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="caneta.caneta"
                    ),
                ),
                (
                    "fornecedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fornecedor.fornecedor",
                    ),
                ),
            ],
        ),
    ]
