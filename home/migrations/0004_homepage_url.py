# Generated by Django 3.0.6 on 2020-05-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='url',
            field=models.URLField(default='http://127.0.0.1'),
            preserve_default=False,
        ),
    ]