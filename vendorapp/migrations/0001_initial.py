# Generated by Django 3.2.9 on 2021-11-18 15:59

from django.db import migrations, models
import location_field.models.plain
import location_field.models.spatial


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', location_field.models.spatial.LocationField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('service', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('land_line', models.CharField(max_length=100)),
                ('aadharImage', models.ImageField(upload_to='Aadhar/')),
                ('panImage', models.ImageField(upload_to='Pan/')),
                ('gstImage', models.ImageField(upload_to='gst/')),
                ('accountNumber', models.CharField(max_length=100)),
                ('bankName', models.CharField(max_length=100)),
                ('ifsc_code', models.CharField(max_length=50)),
                ('accountName', models.CharField(max_length=50)),
                ('otherservice', models.CharField(max_length=50)),
                ('timing', models.DateTimeField(auto_now_add=True)),
                ('about', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='Logo/')),
            ],
        ),
    ]
