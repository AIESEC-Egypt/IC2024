# Generated by Django 4.2.9 on 2024-06-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_description_product_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
