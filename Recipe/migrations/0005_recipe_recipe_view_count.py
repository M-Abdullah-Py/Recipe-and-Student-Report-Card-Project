# Generated by Django 5.1.1 on 2024-10-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0004_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
