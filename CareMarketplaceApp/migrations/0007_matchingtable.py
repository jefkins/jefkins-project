# Generated by Django 5.0.3 on 2024-05-04 10:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CareMarketplaceApp', '0006_remove_caregiverbiodataprofile_postcodeaddress_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchingTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAccepted', models.BooleanField(default=False)),
                ('isCompleted', models.BooleanField(default=False)),
                ('dateCreated', models.DateTimeField()),
                ('dateModified', models.DateTimeField(auto_now_add=True)),
                ('modfiedBy', models.CharField(blank=True, default='Admin', max_length=50, null=True)),
                ('careGiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='care_giver_matching_tables', to=settings.AUTH_USER_MODEL)),
                ('careHome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='care_home_matching_tables', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
