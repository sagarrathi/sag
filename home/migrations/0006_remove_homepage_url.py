# Generated by Django 3.0.6 on 2020-05-26 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200526_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='url',
        ),
    ]
