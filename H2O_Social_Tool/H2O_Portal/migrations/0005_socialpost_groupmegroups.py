# Generated by Django 2.2.7 on 2019-12-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H2O_Portal', '0004_delete_facebookposts'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialpost',
            name='GroupMeGroups',
            field=models.TextField(null=True),
        ),
    ]
