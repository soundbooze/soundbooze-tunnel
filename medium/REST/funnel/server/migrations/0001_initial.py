# Generated by Django 2.2.5 on 2019-09-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Servers',
                'verbose_name': 'Server',
            },
        ),
    ]
