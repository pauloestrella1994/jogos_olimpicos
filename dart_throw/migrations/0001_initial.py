from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DartThrowCompetition',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('competition_name', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('results', models.CharField(default='partial_result', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DartThrowAthletes',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('athlete', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=3, max_digits=6)),
                ('unit_measurement', models.CharField(max_length=2)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_id', to='dart_throw.dartthrowcompetition')),
            ],
            options={
                'ordering': ['-value'],
            },
        ),
    ]
