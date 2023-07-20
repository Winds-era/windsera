# Generated by Django 4.2.3 on 2023-07-20 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_alter_catogaries_id_alter_course_id'),
        ('quiz', '0007_auto_20230718_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.course'),
        ),
    ]