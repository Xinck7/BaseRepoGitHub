# Generated by Django 2.2.6 on 2019-12-07 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H2O_Portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gm_auth_token',
            field=models.TextField(help_text='GroupMe Auth Token', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='insta_auth_token',
            field=models.TextField(help_text='Instagram Auth Token', null=True),
        ),
    ]
