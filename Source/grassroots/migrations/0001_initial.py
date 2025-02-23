# Generated by Django 4.0.5 on 2023-12-06 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('grantID', models.IntegerField(primary_key=True, serialize=False)),
                ('grantName', models.CharField(max_length=255)),
                ('grantAmount', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('userID', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SpecialAward',
            fields=[
                ('awardID', models.IntegerField(primary_key=True, serialize=False)),
                ('awardName', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('eligibility', models.CharField(max_length=255)),
                ('detail', models.TextField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='grassroots.person')),
            ],
            bases=('grassroots.person',),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='grassroots.person')),
            ],
            bases=('grassroots.person',),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('appID', models.IntegerField(primary_key=True, serialize=False)),
                ('detail', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('award', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grassroots.specialaward')),
                ('grant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grassroots.grant')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grassroots.customer')),
            ],
        ),
    ]
