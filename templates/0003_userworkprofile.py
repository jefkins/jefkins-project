# Generated by Django 5.0.3 on 2024-04-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CareMarketplaceApp', '0002_delete_dbusers'),
    ]
    operations = [
        migrations.CreateModel(
            name='UserWorkProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('highestDegreeObtained', models.CharField(max_length=50)),
                ('universityOfStudy', models.CharField(max_length=100)),
                ('dateOfGraduation', models.DateField()),
                ('certifications', models.CharField(max_length=500)),
            ],
        ),
    ]