from django.utils.safestring import mark_safe

from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

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
    
    STYLE_CHOICES = [
        ('syntax', 'default'),
        ('emacs', 'emacs'),
        ('monokai', 'monokai'),
        ('vim', 'vim'),
        ('xcode', 'xcode'),
    ]

    language=blocks.ChoiceBlock(choices=LANGUAGE_CHOICES)
    style=blocks.ChoiceBlock(choices=STYLE_CHOICES)
    code=blocks.TextBlock()

    def render(self, value, context=None):
        src=value['code'].strip("\n")
        lang=value['language']
        lexer=get_lexer_by_name(lang)
        css_class=['code', value['style']]

        formatter=get_formatter_by_name(
            'html',
            linenos=None,
            cssclass=''.join(css_class),
            noclasses=False
        )
        return mark_safe(
            highlight(src, lexer, formatter)
            )

        class Meta:
            icon='code'