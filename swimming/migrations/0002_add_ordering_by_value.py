from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimming', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='swimmingathletes',
            options={'ordering': ['value']},
        ),
    ]
