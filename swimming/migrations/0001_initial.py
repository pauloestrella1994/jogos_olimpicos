# Generated by Django 3.2.7 on 2021-10-04 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SwimmingCompetition',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('competition_name', models.CharField(max_length=200)),
                ('start_date', models.DateField(default='2021-10-04')),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SwimmingAthletes',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('athlete', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=3, max_digits=6)),
                ('unit_measurement', models.CharField(max_length=2)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_id', to='swimming.swimmingcompetition')),
            ],
        ),
    ]
