# Generated by Django 4.1.7 on 2023-07-08 23:30

import bgremove.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=bgremove.models.get_upload_path)),
                ('result', models.ImageField(upload_to=bgremove.models.get_upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default=uuid.uuid4)),
            ],
            options={
                'verbose_name': 'User Activity',
                'verbose_name_plural': 'User Activities',
            },
        ),
    ]
