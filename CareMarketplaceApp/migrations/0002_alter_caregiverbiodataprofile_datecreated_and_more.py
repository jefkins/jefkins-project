# Generated by Django 5.0.3 on 2024-05-02 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CareMarketplaceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caregiverbiodataprofile',
            name='dateCreated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caregivereducationprofile',
            name='dateCreated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caregiverworkexperiencetrainingprofile',
            name='dateCreated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]