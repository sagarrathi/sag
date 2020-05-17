# For categories and other models
from django.db import models

# For importing major class types
from wagtail.core.models import Page
from wagtail.core.models import Orderable

# For Fields And Admin Input
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

#For Tags parental key rplaces forieghn keys
# For major class type:
from taggit.models import TaggedItemBase
# For field type
from modelcluster.contrib.taggit import ClusterTaggableManager
# For Keys:
from modelcluster.fields import ParentalKey


# For Categories adding custom tags
from wagtail.snippets.models import register_snippet
# For Keys:
from modelcluster.fields import ParentalManyToManyField
# For forms
from django import forms

# For  Searching
from wagtail.search import index

####################### Imports Ends Here ###############


class BlogIndexPage(Page):
    intro=RichTextField(blank=True)
    content_panels=Page.content_panels+[
        FieldPanel('intro', classname='full')
    ]

    def get_context(self, request):
        context=super().get_context(request)
        blogpages=self.get_children().live().order_by('-first_published_at')
        context['blogpages']=blogpages

        return context


class BlogPageTag(TaggedItemBase):
    content_object=ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(Page):
    date=models.DateField("Post Date")
    intro=models.CharField(max_length=250)
    body=RichTextField(blank=True)
    tags=ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories=ParentalManyToManyField('blog.BlogCategory', blank=True)

    def main_image(self):
        gallery_item=self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None


    search_fields=Page.search_fields+[
        index.SearchField('intro'),
        index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple)
            ], heading="Blog Information"),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery Images")
    ]


class BlogPageGalleryImage(Orderable):
    page=ParentalKey(BlogPage, 
                    on_delete=models.CASCADE,
                    related_name="gallery_images")

    image=models.ForeignKey('wagtailimages.Image',
                    on_delete=models.CASCADE,
                    related_name='+')

    caption=models.CharField(blank=True, max_length=250)

    panels=[
            ImageChooserPanel('image'),
            FieldPanel('caption')
    ]



class BlogTagIndexPage(Page):
    def get_context(self, request):
        tag=request.GET.get('tag')
        blogpages=BlogPage.objects.filter(tags__name=tag)

        context=super().get_context(request)
        context['blogpages']=blogpages

        return context

@register_snippet
class BlogCategory(models.Model):
    name=models.CharField(max_length=255)
    icon=models.ForeignKey(
        'wagtailimages.Image',null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+')

    # Not using content panels as we do need admin promote tab
    # and other battries
    panels=[
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='blog categories'