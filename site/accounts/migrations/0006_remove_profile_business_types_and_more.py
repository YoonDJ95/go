# Generated by Django 5.1.2 on 2024-10-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_address_alter_profile_detailed_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='business_types',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
