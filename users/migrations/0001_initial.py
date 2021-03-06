# Generated by Django 4.0.4 on 2022-05-31 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=45, unique=True)),
                ('name', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('birth', models.DateField()),
                ('address', models.CharField(max_length=45, null=True)),
                ('agreement', models.JSONField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('take_name', models.CharField(max_length=15)),
                ('take_phonenumber', models.CharField(max_length=15)),
                ('take_homenumber', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=45)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'deliveries',
            },
        ),
    ]
