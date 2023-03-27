# Generated by Django 4.1.7 on 2023-03-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_reservation_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guests',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=16),
        ),
    ]