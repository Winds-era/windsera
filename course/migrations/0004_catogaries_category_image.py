# Generated by Django 4.2.3 on 2023-07-08 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='catogaries',
            name='category_image',
            field=models.ImageField(blank=True, upload_to='Media/course'),
        ),
    ]
