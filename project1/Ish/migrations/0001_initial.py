# Generated by Django 5.0.1 on 2024-01-20 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qurilish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=11)),
                ('location', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Restoran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('limit_age', models.IntegerField(validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(28)])),
                ('position', models.CharField(max_length=25)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=11)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]