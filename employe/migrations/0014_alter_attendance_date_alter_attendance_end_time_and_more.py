# Generated by Django 5.0.2 on 2024-04-02 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0013_alter_attendance_date_alter_attendance_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]