# Generated by Django 5.2 on 2025-04-16 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('businesses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('aisle', models.CharField(choices=[('A1', 'Aisle 1'), ('A2', 'Aisle 2'), ('A3', 'Aisle 3')], max_length=2)),
                ('shelf', models.CharField(choices=[('S1', 'Shelf 1'), ('S2', 'Shelf 2'), ('S3', 'Shelf 3')], max_length=2)),
                ('bay', models.CharField(choices=[('B1', 'Bay 1'), ('B2', 'Bay 2'), ('B3', 'Bay 3')], max_length=2)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='businesses.business')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('unit_type', models.CharField(choices=[('perishable', 'Perishable'), ('non_perishable', 'Non-Perishable'), ('hazardous', 'Hazardous'), ('non-hazardous', 'Non-Hazardous')], max_length=50)),
                ('received_date', models.DateField()),
                ('pick_date', models.DateField(blank=True, null=True)),
                ('exp_date', models.DateField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('taxable', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='businesses.business')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units', to='inventory.location')),
            ],
        ),
    ]
