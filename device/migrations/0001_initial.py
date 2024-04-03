# Generated by Django 5.0.3 on 2024-04-03 13:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serial_no', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('L', 'Laptop'), ('S', 'Smartphone'), ('T', 'Tablet'), ('M', 'Monitor'), ('K', 'Keyboard'), ('H', 'Headset'), ('N', 'Null')], max_length=1)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
            ],
        ),
        migrations.CreateModel(
            name='AddDeviceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('C', 'Checked Out'), ('R', 'Returned')], max_length=1)),
                ('condition', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
            ],
        ),
    ]