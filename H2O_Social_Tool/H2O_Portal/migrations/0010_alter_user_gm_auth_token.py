# Generated by Django 3.2.2 on 2021-05-30 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H2O_Portal', '0009_alter_user_gm_auth_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gm_auth_token',
            field=models.CharField(blank=True, help_text='GroupMe Authentication Token', max_length=30, null=True),
        ),
    ]
