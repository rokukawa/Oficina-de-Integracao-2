# Generated by Django 4.1 on 2022-10-01 17:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("caneta", "0004_alter_caneta_modelo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="caneta",
            name="cor",
            field=models.CharField(
                max_length=45, validators=[django.core.validators.MinLengthValidator(5)]
            ),
        ),
        migrations.AlterField(
            model_name="caneta",
            name="ponta",
            field=models.CharField(
                max_length=45, validators=[django.core.validators.MinLengthValidator(5)]
            ),
        ),
    ]
