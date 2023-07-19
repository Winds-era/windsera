# Generated by Django 2.2.7 on 2023-07-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0009_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='plan',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Super', 'Super'), ('Pro', 'Pro')], default='Basic', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]