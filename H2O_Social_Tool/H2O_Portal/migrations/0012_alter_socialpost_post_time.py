# Generated by Django 3.2.2 on 2021-05-30 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H2O_Portal', '0011_alter_user_gm_auth_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialpost',
            name='post_time',
            field=models.DateTimeField(help_text='Type date or click icon to select a date:', max_length=30),
        ),
    ]
