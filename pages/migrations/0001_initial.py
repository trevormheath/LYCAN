# Generated by Django 4.1.2 on 2022-11-16 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=30)),
                ('lName', models.CharField(max_length=30)),
                ('funfact', models.CharField(blank=True, max_length=255)),
                ('sectionNum', models.IntegerField()),
                ('groupNum', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('photoUrl', models.CharField(max_length=500)),
                ('feedback', models.CharField(blank=True, max_length=300)),
            ],
            options={
                'db_table': 'current_students',
            },
        ),
    ]
