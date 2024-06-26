# Generated by Django 4.1.6 on 2023-11-17 08:02

from django.conf import settings
import django.core.validators
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
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=20)),
                ('passwd', models.CharField(blank=True, max_length=50, verbose_name='Passwd')),
                ('trade_status', models.CharField(choices=[('INACTIVE', 'INACTIVE'), ('ACTIVE', 'ACTIVE')], default='INACTIVE', max_length=50, verbose_name='Trade status')),
                ('trading_plan', models.CharField(choices=[('NO PLAN', 'NO PLAN'), ('STARTER', 'STARTER'), ('BRONZE', 'BRONZE'), ('SILVER', 'SILVER'), ('GOLD', 'GOLD'), ('DIAMOND', 'DIAMOND'), ('PLATINUM', 'PLATINUM')], default='NO PLAN', max_length=50, verbose_name='Trading plan')),
                ('deposit_balance', models.IntegerField(default=50, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Deposit_Balance')),
                ('profit_balance', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Profit Balance')),
                ('country', models.CharField(default='none', max_length=50, verbose_name='Country')),
                ('document_front', models.ImageField(upload_to='images/')),
                ('document_back', models.ImageField(upload_to='images/')),
                ('passport', models.ImageField(upload_to='images/')),
                ('verify', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Withdrawal_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Deposit Balance')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('SUCCESS', 'SUCCESS')], default='PENDING', max_length=50, verbose_name='Deposit Status')),
                ('method', models.CharField(default='BITCOIN', max_length=50, verbose_name='Deposit Method')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Deposit Balance')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('SUCCESS', 'SUCCESS')], default='PENDING', max_length=50, verbose_name='Deposit Status')),
                ('method', models.CharField(default='BITCOIN', max_length=50, verbose_name='Deposit Method')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
