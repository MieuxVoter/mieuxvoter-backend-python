# Generated by Django 2.2.1 on 2019-06-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0006_election_num_grades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='num_grades',
            field=models.SmallIntegerField(verbose_name='Num. grades'),
        ),
    ]
