# Generated by Django 5.0.2 on 2024-05-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0021_skillset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillset',
            name='user',
        ),
        migrations.AddField(
            model_name='skillset',
            name='id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]