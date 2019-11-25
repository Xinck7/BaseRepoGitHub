# Generated by Django 2.2.7 on 2019-11-25 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('H2O_Portal', '0002_post_updated_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=200)),
                ('post_time', models.DateTimeField(max_length=30)),
                ('message', models.TextField(blank=True, max_length=2000)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('Facebook', models.BooleanField(default=False)),
                ('Instagram', models.BooleanField(default=False)),
                ('GroupMe', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
