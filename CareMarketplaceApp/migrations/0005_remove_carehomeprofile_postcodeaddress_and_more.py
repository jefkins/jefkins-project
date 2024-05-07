# Generated by Django 5.0.3 on 2024-05-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CareMarketplaceApp', '0004_remove_caregiverworkexperienceprofile_otherlanguage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carehomeprofile',
            name='postCodeAddress',
        ),
        migrations.AlterField(
            model_name='caregiverbiodataprofile',
            name='address',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='caregiverbiodataprofile',
            name='city',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='caregiverbiodataprofile',
            name='state',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carehomeprofile',
            name='address',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='carehomeprofile',
            name='city',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carehomeprofile',
            name='country',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carehomeprofile',
            name='state',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
    ]
