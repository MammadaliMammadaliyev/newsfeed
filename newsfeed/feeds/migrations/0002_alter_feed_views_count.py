# Generated by Django 5.0.1 on 2024-01-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='views_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]