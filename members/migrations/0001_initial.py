# Generated by Django 3.1.2 on 2023-12-31 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('mobile_number', models.CharField(max_length=10, unique=True, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('medical_history', models.CharField(blank=True, default='None', max_length=300, verbose_name='Medical History')),
                ('admitted_on', models.DateField(auto_now_add=True)),
                ('registration_date', models.DateField(default='dd/mm/yyyy', verbose_name='Registration Date')),
                ('registration_upto', models.DateField()),
                ('dob', models.DateField(default='dd/mm/yyyy')),
                ('subscription_type', models.CharField(choices=[('INE1', 'INE1'), ('INE2', 'INE2'), ('INE3', 'INE3'), ('Master', 'Master')], default='INE1', max_length=30, verbose_name='Subscription Type')),
                ('subscription_period', models.CharField(choices=[('1', '1 mois'), ('2', '2 mois'), ('3', '3 mois'), ('4', '4 mois'), ('5', '5 mois'), ('6', '6 mois'), ('7', '7 mois'), ('8', '8 mois'), ('7', '9 mois')], default='1', max_length=30, verbose_name='Subscription Period')),
                ('filiere', models.CharField(choices=[('DATA', 'DATA'), ('DIGITAL', 'DIGITAL'), ('EMBARQUé', 'EMBARQUé'), ('SMART', 'SMART'), ('CLOUD', 'CLOUD'), ('CYBER', 'CYBER'), ('AMOA', 'AMOA'), ('BIGDATA', 'BIGDATA')], default='DATA', max_length=30, verbose_name='filiere')),
                ('amount', models.CharField(max_length=30)),
                ('fee_status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending')], default='paid', max_length=30, verbose_name='Fee Status')),
                ('genre', models.CharField(choices=[('H', 'HOMME'), ('F', 'FEMME')], default='H', max_length=30, verbose_name='genre')),
                ('photo', models.FileField(blank=True, upload_to='photos/')),
                ('notification', models.IntegerField(blank=True, default=2)),
                ('stop', models.IntegerField(blank=True, choices=[(0, 'Start'), (1, 'Stop')], default=0, verbose_name='Status')),
            ],
        ),
    ]