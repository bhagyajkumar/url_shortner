# Generated by Django 4.0.5 on 2022-06-04 12:40

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_url_clicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.URLField(validators=[main.models.validate_url]),
        ),
    ]
