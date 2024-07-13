# Generated by Django 5.0.6 on 2024-07-12 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SuperMarketSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.branch')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.country')),
                ('customer_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.customertype')),
                ('gender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.gender')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.payment')),
                ('productline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.productline')),
            ],
        ),
    ]
