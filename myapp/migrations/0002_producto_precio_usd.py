# Generated by Django 5.0 on 2024-06-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_usd',
            field=models.FloatField(blank=True, null=True),
        ),
    ]