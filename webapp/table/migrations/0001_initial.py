# Generated by Django 4.2.1 on 2023-05-25 13:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('users', models.ManyToManyField(blank=True, related_name='tables', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
