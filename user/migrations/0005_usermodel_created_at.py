# Generated by Django 4.1.7 on 2023-04-07 00:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_usermodel_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
