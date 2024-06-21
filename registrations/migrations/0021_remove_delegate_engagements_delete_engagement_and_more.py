# Generated by Django 4.2.9 on 2024-02-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0020_rename_room_with_the_same_gender_delegate_room_preference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delegate',
            name='engagements',
        ),
        migrations.DeleteModel(
            name='Engagement',
        ),
        migrations.AddField(
            model_name='delegate',
            name='engagements',
            field=models.CharField(blank=True, choices=[(None, '-------'), ('Worlds largest lesson', 'Worlds largest lesson'), ('Keynote', 'Keynote'), ('Workshop', 'Workshop'), ('Networking spaces', 'Networking spaces'), ('Other', 'Other')], max_length=50, null=True),
        ),
    ]