# Generated by Django 3.0.6 on 2020-05-17 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogpage_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name_plural': 'blog categories'},
        ),
    ]
