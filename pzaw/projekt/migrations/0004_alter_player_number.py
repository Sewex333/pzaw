# Generated by Django 5.1.4 on 2025-01-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0003_player_number_alter_player_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.PositiveIntegerField(),
        ),
    ]
