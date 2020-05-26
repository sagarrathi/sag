from django.http import HttpResponse

from django.utils.safestring import mark_safe

from wagtail.core import blocks

class CodeBlock(blocks.StructBlock):
    LANGUAGE_CHOICES = [
        ('markup','Markup'),
        ('css','CSS'),
        ('clike','Clike'),
        ('javascript','Javascript'),
        ('bash','Bash'),
        ('basic','Basic'),
        ('django','Django'),
        ('dns-zone-file','DNS-Zone-File'),
        ('git','Git'),
        ('markup-templating','Markup-Templating'),
        ('nginx','Nginx'),
        ('python','Python'),
        ('r','R'),
        ('jsx','Jsx'),
        ('tsx','Tsx'),
        ('sql','Sql'),
        ('typescript','Typescript'),
        ('visual-basic','Visual-Basic'),

        ]
    
    
    language=blocks.ChoiceBlock(choices=LANGUAGE_CHOICES)
    code=blocks.TextBlock()       

    class Meta:
        template="blog/blocks/code_block.html"
        icon="code"
        label="Code" 


class MathBlock(blocks.StructBlock):
      
    math=blocks.TextBlock()       

    class Meta:
        template="blog/blocks/math_block.html"
        icon="math"
        label="Math" 
