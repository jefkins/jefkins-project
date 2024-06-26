# Generated by Django 5.0.3 on 2024-04-30 12:11

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CareGiverWorkExperienceProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutSelf', models.TextField(blank=True, null=True)),
                ('typeOfCareExperience', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('availability', models.CharField(blank=True, choices=[('fullTime', 'Full Time'), ('partTime', 'Part Time')], max_length=50, null=True)),
                ('PrimaryLanguage', models.CharField(choices=[('English', 'English'), ('French', 'French'), ('Spanish', 'Spanish'), ('Chinese', 'Chinese'), ('Deutch', 'Deutch'), ('Others', 'Others')], max_length=50, verbose_name='Primary Language')),
                ('PrimaryLanguageProfeciency', models.CharField(choices=[('Beginner', 'Beginner'), ('Intemediate', 'Intemediate'), ('Expert', 'Expert'), ('Native', 'Native')], max_length=50, verbose_name='Primary Language Profeciency')),
                ('SecondaryLanguage', models.CharField(choices=[('English', 'English'), ('French', 'French'), ('Spanish', 'Spanish'), ('Chinese', 'Chinese'), ('Deutch', 'Deutch'), ('Others', 'Others')], max_length=50, verbose_name='Secondary Language')),
                ('SecondaryLanguageProfeciency', models.CharField(choices=[('Beginner', 'Beginner'), ('Intemediate', 'Intemediate'), ('Expert', 'Expert'), ('Native', 'Native')], max_length=50, verbose_name='Secondary Language Profeciency')),
                ('OtherLanguage', models.CharField(choices=[('English', 'English'), ('French', 'French'), ('Spanish', 'Spanish'), ('Chinese', 'Chinese'), ('Deutch', 'Deutch'), ('Others', 'Others')], max_length=50, verbose_name='Other Language')),
                ('OtherLanguageProfeciency', models.CharField(choices=[('Beginner', 'Beginner'), ('Intemediate', 'Intemediate'), ('Expert', 'Expert'), ('Native', 'Native')], max_length=50, verbose_name='Other Language Profeciency')),
            ],
        ),
        migrations.CreateModel(
            name='CareGiverBioDataProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.CharField(blank=True, choices=[('CareGiver', 'Care Giver'), ('CareHome', 'Care Home')], max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=500, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('primary_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('secondary_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='Media_Files/profile_pictures/')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('postCodeAddress', models.CharField(blank=True, max_length=200, null=True)),
                ('postCodeLongitude', models.CharField(blank=True, max_length=200, null=True)),
                ('postCodeLatitude', models.CharField(blank=True, max_length=50, null=True)),
                ('dateCreated', models.DateTimeField()),
                ('dateModified', models.DateTimeField(auto_now_add=True)),
                ('modfiedBy', models.CharField(blank=True, max_length=50, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('userAuth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CareGiverEducationProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highestDegreeObtained', models.CharField(blank=True, choices=[('NoDegree', 'Non Academic'), ('OLevel', 'Olevel'), ('Undergratuate', 'Undergraduate Degree'), ('Masters', 'Masters Degree'), ('Phd', 'PHD Degree')], max_length=50, null=True, verbose_name='Highest Degree Obtained')),
                ('CourseOfStudy', models.CharField(blank=True, max_length=100, null=True, verbose_name='Eg B.Sc Nursing, Diploma Adult Care')),
                ('dateCreated', models.DateTimeField()),
                ('dateModified', models.DateTimeField(auto_now_add=True)),
                ('modfiedBy', models.CharField(blank=True, max_length=50, null=True)),
                ('userAuth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CareGiverWorkExperienceTrainingProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOfCareExperience', models.CharField(blank=True, max_length=100, null=True)),
                ('trainedOnCareExperience', models.BooleanField(blank=True, null=True)),
                ('trainingCertificate', models.ImageField(upload_to='Media_Files/Certificates')),
                ('dateCreated', models.DateTimeField()),
                ('dateModified', models.DateTimeField(auto_now_add=True)),
                ('modfiedBy', models.CharField(blank=True, max_length=50, null=True)),
                ('userAuth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CareHomeProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.CharField(blank=True, choices=[('CareGiver', 'Care Giver'), ('CareHome', 'Care Home')], max_length=50, null=True)),
                ('name_0f_care_home', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('primary_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('secondary_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('postCodeAddress', models.CharField(blank=True, max_length=200, null=True)),
                ('postCodeLongitude', models.CharField(blank=True, max_length=200, null=True)),
                ('postCodeLatitude', models.CharField(blank=True, max_length=50, null=True)),
                ('dateCreated', models.DateTimeField()),
                ('dateModified', models.DateTimeField(auto_now_add=True)),
                ('modfiedBy', models.CharField(blank=True, max_length=50, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('userAuth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
