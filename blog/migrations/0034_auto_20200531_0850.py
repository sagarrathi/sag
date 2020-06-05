# Generated by Django 3.0.6 on 2020-05-31 08:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20200531_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='apps',
            field=wagtail.core.fields.StreamField([('inputs', wagtail.core.blocks.StructBlock([('file_type', wagtail.core.blocks.ChoiceBlock(choices=[('Image', 'image'), ('Text', 'text'), ('Video', 'video'), ('Excel', 'excel'), ('CSV', 'csv')])), ('file_id', wagtail.core.blocks.IntegerBlock())])), ('outputs', wagtail.core.blocks.StructBlock([('file_type', wagtail.core.blocks.ChoiceBlock(choices=[('Image', 'image'), ('Text', 'text'), ('Video', 'video'), ('Excel', 'excel'), ('CSV', 'csv')])), ('file_id', wagtail.core.blocks.IntegerBlock())]))], null=True),
        ),
    ]