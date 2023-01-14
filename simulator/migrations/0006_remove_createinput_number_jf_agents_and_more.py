# Generated by Django 4.0.2 on 2023-01-14 11:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0005_createinput_uuid_alter_globalresults_shift_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createinput',
            name='number_jf_agents',
        ),
        migrations.AddField(
            model_name='createinput',
            name='number_of_agents',
            field=models.IntegerField(default=20, help_text='number of people handling calls', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='c_h',
            field=models.FloatField(default=10, help_text=' maximum amount of time, in seconds, required to enter the results of a conversation into the system', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='c_l',
            field=models.FloatField(default=4, help_text='minimum amount of time, in seconds, required to enter the results of a conversation into the system', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='call_list',
            field=models.IntegerField(default=10000, help_text='number of clients that need to be contacted', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(40000)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='d_h',
            field=models.FloatField(default=10, help_text='longest duration, in seconds, that the system takes to detect answering machine', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='d_l',
            field=models.FloatField(default=1, help_text='shortest duration, in seconds, that the system takes to detect answering machine', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='d_m',
            field=models.FloatField(default=4, help_text='average duration, in seconds, that the system takes to detect answering machine', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='line_numbers',
            field=models.IntegerField(default=100, help_text='number of lines assigned to your call center', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='number_of_simulations',
            field=models.IntegerField(default=1, help_text='how many times the entire process is repeated', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='p_h',
            field=models.FloatField(default=15, help_text='longest duration, in seconds, that a customer is willing to wait for an agent after answering the call', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='p_l',
            field=models.FloatField(default=6, help_text='shortest duration, in seconds, that a customer is willing to wait for an agent after answering the call', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='reach_rate_h',
            field=models.FloatField(default=0.5, help_text='highest percentage of customers who answered the call out of those who received it', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='reach_rate_l',
            field=models.FloatField(default=0.01, help_text='lowest percentage of customers who answered the call out of those who received it', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='reach_rate_m',
            field=models.FloatField(default=0.3, help_text='average percentage of customers who answered the call out of those who received it', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='ring_time_h',
            field=models.FloatField(default=45, help_text='maximum longest duration, in seconds, that a call will ring before being considered as unanswered', validators=[django.core.validators.MinValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='ring_time_l',
            field=models.FloatField(default=5, help_text='shortest duration, in seconds, that a call will ring before being considered as unanswered', validators=[django.core.validators.MinValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='ring_time_m',
            field=models.FloatField(default=15, help_text='average duration, in seconds, that a call will ring before being considered as unanswered', validators=[django.core.validators.MinValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='shift_time',
            field=models.FloatField(default=8, help_text='duration of the shift, measured in hours', validators=[django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='t_h',
            field=models.FloatField(default=90, help_text='longest duration, in seconds, of a conversation between a client and an agent', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='t_l',
            field=models.FloatField(default=2, help_text='shortest duration, in seconds, of a conversation between a client and an agent', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='take_high',
            field=models.FloatField(default=4, help_text='maximum time it takes to load the dialer, measured in seconds', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='take_low',
            field=models.FloatField(default=2, help_text='minimum time it takes to load the dialer, measured in seconds', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='take_mode',
            field=models.FloatField(default=3, help_text='average time it takes to load the dialer, measured in seconds', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='unreachable_h',
            field=models.FloatField(default=0.3, help_text='maximum percentage of unsuccessful attempts in a batch', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='unreachable_l',
            field=models.FloatField(default=0.1, help_text='minimum percentage of unsuccessful attempts in a batch', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='createinput',
            name='unreachable_m',
            field=models.FloatField(default=0.2, help_text='average percentage of unsuccessful attempts in a batch', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
