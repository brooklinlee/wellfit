# Generated by Django 4.2.7 on 2023-11-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_set_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='workout_type',
            field=models.CharField(choices=[('cardio', 'Cardio'), ('strength', 'Strength Training'), ('flexibility', 'Flexibility'), ('endurance', 'Endurance'), ('HIIT', 'High-Intensity Interval Training'), ('yoga', 'Yoga'), ('pilates', 'Pilates'), ('crossfit', 'CrossFit'), ('swimming', 'Swimming'), ('cycling', 'Cycling'), ('running', 'Running'), ('walking', 'Walking'), ('aerobics', 'Aerobics'), ('weightlifting', 'Weightlifting'), ('calisthenics', 'Calisthenics'), ('other', 'Other')], default='cardio', max_length=20),
        ),
    ]
