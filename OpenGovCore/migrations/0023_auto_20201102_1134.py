# Generated by Django 3.1 on 2020-11-02 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenGovCore', '0022_auto_20201030_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='assembly_sessions',
            name='session_name',
            field=models.CharField(blank=True, choices=[('Monsoon Session', 'Monsoon Session'), ('Budget Session', 'Budget Session'), ('Winter Session', 'Winter Session')], max_length=100),
        ),
        migrations.AddField(
            model_name='parliamentary_sessions',
            name='session_name',
            field=models.CharField(blank=True, choices=[('Monsoon Session', 'Monsoon Session'), ('Budget Session', 'Budget Session'), ('Winter Session', 'Winter Session')], max_length=100),
        ),
        migrations.AlterField(
            model_name='assembly_sessions',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='assembly_sessions',
            name='start_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='parliamentary_sessions',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='parliamentary_sessions',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]
