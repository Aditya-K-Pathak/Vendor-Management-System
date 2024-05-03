# Generated by Django 5.0.3 on 2024-05-03 12:40

import VendorProfile.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VendorProfile',
            fields=[
                ('vendor_code', models.CharField(default=VendorProfile.models.generate_vendor_code, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('vendor_name', models.CharField(max_length=100)),
                ('contact_number', models.IntegerField(max_length=10, unique=True)),
                ('address', models.TextField()),
                ('new_orders', models.JSONField(default={})),
                ('orders_received', models.IntegerField(default=0)),
                ('orders_fulfilled', models.IntegerField(default=0)),
                ('fulfillment_rate', models.FloatField(default=0)),
                ('on_time_delivery', models.IntegerField(default=0)),
                ('on_time_delivery_rate', models.FloatField(default=0)),
                ('quality_rating_avg', models.FloatField(default=0)),
                ('avg_response_time', models.DurationField(default=None, null=True)),
                ('total_rating', models.IntegerField(default=0)),
                ('ratings_given', models.IntegerField(default=0)),
                ('orders_cancelled', models.IntegerField(default=0)),
            ],
        ),
    ]