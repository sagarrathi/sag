from django.utils.html import format_html

from django.utils.safestring import mark_safe

from wagtail.core import blocks

class CodeBlock(blocks.StructBlock):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('bash', 'Bash/Shell'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('scss', 'SCSS'),
        ('json', 'JSON'),
        ]
    
    
    language=blocks.ChoiceBlock(choices=LANGUAGE_CHOICES)
    code=blocks.TextBlock()       
   

    class Meta:
        template="blog/blocks/code_block.html"
        icon="code"
        label="Code" 
