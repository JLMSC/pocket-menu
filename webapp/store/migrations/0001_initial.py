# Generated by Django 4.2.1 on 2023-05-23 21:45

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('cnpj', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator('^[0-9]{14}$', 'CNPJ inválido')])),
                ('postal_code', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^[0-9]{8}$', 'CEP inválido')])),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(choices=[('ac', 'AC'), ('al', 'AL'), ('ap', 'AP'), ('am', 'AM'), ('ba', 'BA'), ('ce', 'CE'), ('es', 'ES'), ('go', 'GO'), ('ma', 'MA'), ('mt', 'MT'), ('ms', 'MS'), ('mg', 'MG'), ('pa', 'PA'), ('pb', 'PB'), ('pr', 'PR'), ('pe', 'PE'), ('pi', 'PI'), ('rj', 'RJ'), ('rn', 'RN'), ('rs', 'RS'), ('ro', 'RO'), ('rr', 'RR'), ('sc', 'SC'), ('sp', 'SP'), ('se', 'SE'), ('to', 'TO'), ('df', 'DF')], max_length=2)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name_plural': 'stores',
                'ordering': ['id'],
            },
        ),
    ]
