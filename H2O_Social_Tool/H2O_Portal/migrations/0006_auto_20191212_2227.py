# Generated by Django 3.0 on 2019-12-13 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H2O_Portal', '0005_auto_20191212_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gm_auth_token',
            field=models.TextField(blank=True, help_text='GroupMe Authentication Token', null=True),
        ),
    ]
