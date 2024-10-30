# Generated by Django 5.1.1 on 2024-10-02 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0005_recipe_recipe_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StudentID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.EmailField(max_length=254, unique=True)),
                ('student_address', models.TextField()),
                ('student_age', models.IntegerField(default=18)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='Recipe.department')),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='Recipe.studentid')),
            ],
            options={
                'verbose_name': 'student',
                'ordering': ['student_name'],
            },
        ),
    ]
