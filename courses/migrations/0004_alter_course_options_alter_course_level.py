# Generated by Django 4.0.1 on 2022-01-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_category_lesson_remove_coursesection_episodes_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'get_latest_by': 'created_at'},
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], default='Beginner', max_length=20),
        ),
    ]
