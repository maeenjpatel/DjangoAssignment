# Generated by Django 4.0.4 on 2023-06-07 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QueryForm',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('dept', models.CharField(max_length=100)),
                ('sem', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=10)),
                ('desc', models.TextField()),
            ],
        ),
    ]
