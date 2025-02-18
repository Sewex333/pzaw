# Generated by Django 5.1.4 on 2025-01-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0002_club_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='number',
            field=models.PositiveIntegerField(default=0, max_length=99),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(max_length=100),
        ),
    ]
