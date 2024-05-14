# Generated by Django 5.0.4 on 2024-05-14 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_remove_course_lesson_name_delete_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=150, verbose_name='Название урока')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='materials/')),
                ('description', models.TextField(verbose_name='Описание')),
                ('link_to_the_video', models.TextField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='Название урока')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ('id',),
            },
        ),
    ]