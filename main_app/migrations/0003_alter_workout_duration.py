# Generated by Django 4.2.7 on 2023-11-03 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_workout_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='duration',
            field=models.CharField(choices=[('15 Minutes', '15 Minutes'), ('30 Minutes', '30 Minutes'), ('45 Minutes', '45 Minutes'), ('1 Hour', '1 Hour'), ('1.5 Hours', '1.5 Hours'), ('2 Hours', '2 Hours'), ('More than 2 Hours', 'More than 2 Hours')], default='15 Minutes', max_length=50),
        ),
    ]
