# Generated by Django 2.2.1 on 2019-05-21 20:02

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0003_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='on_invitation_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='election',
            name='candidates',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255, verbose_name='Name'), size=None),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.CharField(db_index=True, max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('used', models.BooleanField(default=False, verbose_name='Used')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.Election')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]