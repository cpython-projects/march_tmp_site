# Generated by Django 4.1.7 on 2023-03-14 06:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Phone number is waited in format +380xx xxx xx xx', regex='^+?3?8?0?\\d{2}[- ]?(\\d[ -]?){7}$')])),
                ('date', models.DateTimeField()),
                ('date_request', models.DateTimeField(auto_now_add=True)),
                ('date_response', models.DateTimeField(auto_now=True)),
                ('guests', models.PositiveSmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=1000)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date_request',),
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
                ('is_special', models.BooleanField(default=False)),
                ('is_signature', models.BooleanField(default=False)),
                ('desc', models.TextField(blank=True, max_length=200, verbose_name='about dish')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discount', models.PositiveSmallIntegerField(default=0)),
                ('ingredients', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='dishes')),
                ('is_recommended', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='main_app.dishcategory')),
            ],
            options={
                'verbose_name': 'Dish',
                'verbose_name_plural': 'Dishes',
                'ordering': ('position',),
            },
        ),
    ]