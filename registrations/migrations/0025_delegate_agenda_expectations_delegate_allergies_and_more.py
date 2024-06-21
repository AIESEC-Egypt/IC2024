# Generated by Django 4.2.9 on 2024-04-12 22:12

from django.db import migrations, models
import registrations.models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0024_remove_delegate_picture_of_the_delegate'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegate',
            name='agenda_expectations',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='allergies',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='cc_team_expecations',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='current_living_country_territory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='egyptian_nights_expectations',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='food',
            field=models.ManyToManyField(to='registrations.food'),
        ),
        migrations.AddField(
            model_name='delegate',
            name='logistical_expectations',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='merchandise',
            field=models.CharField(blank=True, choices=[(None, '-------'), ('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='name_as_per_passport',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='natonality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='passport_expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='passport_issue_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='passport_scanned_photo',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[registrations.models.validate_image_size]),
        ),
        migrations.AddField(
            model_name='delegate',
            name='picture_of_the_delegate',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[registrations.models.validate_image_size]),
        ),
        migrations.AddField(
            model_name='delegate',
            name='pre_and_post_trips',
            field=models.CharField(blank=True, choices=[(None, 'Your trips preference'), ('Pre-conference trip', 'Pre-conference trip'), ('Post-conference trip', 'Post-conference trip'), ('Both', 'Both'), ('None', 'None')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='room_preference',
            field=models.CharField(blank=True, choices=[(None, 'Your room preference'), ('Female only', 'Female only'), ('Male only', 'Male only'), ('Female preferred', 'Female preferred'), ('Male preferred', 'Male preferred'), ('Mixed', 'Mixed')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='visa_support',
            field=models.CharField(blank=True, choices=[(None, '-------'), ('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
    ]