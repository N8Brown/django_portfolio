# Generated by Django 3.1.7 on 2021-03-05 00:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20210304_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='html',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='use_html',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='use_screenshots',
            field=models.BooleanField(default=True),
        ),
    ]
