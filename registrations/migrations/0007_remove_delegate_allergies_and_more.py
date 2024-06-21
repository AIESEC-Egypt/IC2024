# Generated by Django 4.2.9 on 2024-02-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0006_delegate_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delegate',
            name='allergies',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='diet_restrictions',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='entity',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='reasons_to_attend',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='spicy_food',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='vegan',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='position',
        ),
        migrations.DeleteModel(
            name='Allergies',
        ),
        migrations.DeleteModel(
            name='Diet',
        ),
        migrations.DeleteModel(
            name='Entity',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.DeleteModel(
            name='ReasonToAttend',
        ),
        migrations.DeleteModel(
            name='Spicy',
        ),
        migrations.DeleteModel(
            name='Vegan',
        ),
        migrations.AddField(
            model_name='delegate',
            name='position',
            field=models.CharField(choices=[('MCP', 'MCP'), ('MCVP', 'MCVP'), ('LCP', 'LCP')], max_length=30, null=True),
        ),
    ]
