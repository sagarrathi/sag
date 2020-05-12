from django.db import models

from wagtail.core.models import Page

## Text field and Field Panel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import  FieldPanel
####

class HomePage(Page):
    body=RichTextField(blank  = True)

    content_panels =Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]