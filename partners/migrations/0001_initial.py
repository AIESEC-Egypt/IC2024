# Generated by Django 4.2.9 on 2024-04-14 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('company_field', models.CharField(blank=True, max_length=200, null=True)),
                ('company_size', models.CharField(blank=True, choices=[(None, '------'), ('10-50 Employee', '10-50 Employee'), ('50-100 Emmployee', '50-100 Emmployee'), ('100-300 Employee', '100-300 Employee'), ('300+ Employee', '300+ Employee')], max_length=200, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('reason_for_interest', models.CharField(blank=True, max_length=200, null=True)),
                ('person_name', models.CharField(blank=True, max_length=200, null=True)),
                ('person_email', models.EmailField(blank=True, max_length=200, null=True)),
                ('person_mobile', models.CharField(blank=True, max_length=200, null=True)),
                ('person_position', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
