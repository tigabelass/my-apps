# Generated by Django 5.1.1 on 2024-10-05 12:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(max_length=255)),
                ('result', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
