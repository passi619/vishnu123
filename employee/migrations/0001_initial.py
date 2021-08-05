# Generated by Django 3.2.5 on 2021-08-05 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('cName', models.CharField(max_length=50, primary_key='true', serialize=False, unique='true')),
                ('cEmail', models.EmailField(max_length=254)),
                ('cPhone', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eFname', models.CharField(max_length=50, primary_key='true', serialize=False, unique='true')),
                ('eLname', models.CharField(max_length=50)),
                ('eEmail', models.EmailField(max_length=254)),
                ('ePhone', models.CharField(max_length=50)),
                ('eDepartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.department')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]