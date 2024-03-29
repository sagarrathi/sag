# Generated by Django 3.0.6 on 2020-05-26 05:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20200525_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('para', wagtail.core.blocks.RichTextBlock(blank=True)), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('markup', 'Markup'), ('css', 'CSS'), ('clike', 'Clike'), ('javascript', 'Javascript'), ('bash', 'Bash'), ('basic', 'Basic'), ('django', 'Django'), ('dns-zone-file', 'DNS-Zone-File'), ('git', 'Git'), ('markup-templating', 'Markup-Templating'), ('nginx', 'Nginx'), ('python', 'Python'), ('r', 'R'), ('jsx', 'Jsx'), ('tsx', 'Tsx'), ('sql', 'Sql'), ('typescript', 'Typescript'), ('visual-basic', 'Visual-Basic')])), ('code', wagtail.core.blocks.TextBlock())])), ('math', wagtail.core.blocks.StructBlock([('math', wagtail.core.blocks.TextBlock())]))]),
        ),
    ]
