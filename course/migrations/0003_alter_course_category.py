# Generated by Django 4.2.3 on 2023-07-08 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_author_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.catogaries'),
        ),
    ]