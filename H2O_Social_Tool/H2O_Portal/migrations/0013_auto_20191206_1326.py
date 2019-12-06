# Generated by Django 2.2.7 on 2019-12-06 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('H2O_Portal', '0012_auto_20191206_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookstatus',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='H2O_Portal.User'),
        ),
        migrations.AlterField(
            model_name='socialpost',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='H2O_Portal.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='accounts',
            field=models.ManyToManyField(related_name='_user_accounts_+', to='H2O_Portal.User'),
        ),
    ]
