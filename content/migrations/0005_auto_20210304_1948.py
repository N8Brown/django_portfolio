# Generated by Django 3.1.7 on 2021-03-05 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20210304_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='alt_text2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='alt_text3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='alt_text4',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
