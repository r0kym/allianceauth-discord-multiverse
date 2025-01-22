# Generated by Django 4.2.16 on 2024-10-16 22:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aadiscordmultiverse', '0007_remove_discordmanagedserver_ignored_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerActiveFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('reversed_logic', models.BooleanField(default=False, help_text='If set all members WITHOUT an account will pass the test.')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aadiscordmultiverse.discordmanagedserver')),
            ],
            options={
                'verbose_name': 'Smart Filter: Discord Server Active Loaded',
                'verbose_name_plural': 'Smart Filter: Discord Server Active Loaded',
            },
        ),
    ]
