# Generated by Django 4.0.2 on 2023-01-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0004_globalresults_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='createinput',
            name='uuid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='globalresults',
            name='shift_finished',
            field=models.CharField(max_length=100, null=True),
        ),
    ]