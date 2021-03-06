# Generated by Django 2.0.6 on 2018-06-19 20:26

from django.db import migrations, models

# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# persons.migrations.0003_person_full_name_data


class Migration(migrations.Migration):

    replaces = [
        ('persons', '0001_initial'),
        ('persons', '0002_person_full_name'),
        ('persons', '0003_person_full_name_data'),
        ('persons', '0004_remove_first_last_name'),
    ]

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('full_name', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.RunPython(
            code=persons.migrations.0003_person_full_name_data.combine_names,
        ),
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
    ]
