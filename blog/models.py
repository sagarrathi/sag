# For categories and other models
from django.db import models
from django.shortcuts import render


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
# For listing TAG objects
from taggit.models import Tag
from django.contrib.contenttypes.models import ContentType


# For Categories adding custom tags
from wagtail.snippets.models import register_snippet
# For Keys:
from modelcluster.fields import ParentalManyToManyField
# For forms
from django import forms

# For Routable Index Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

# For  Searching
from wagtail.search import index
from wagtail.search.models import Query
    
####################### Imports Ends Here ###############


class BlogIndexPage(RoutablePageMixin,Page):
    intro=RichTextField(blank=True)
    content_panels=Page.content_panels+[
        FieldPanel('intro', classname='full')
    ]

    def get_context(self, request,*args, **kwargs):
        context=super().get_context(request,*args, **kwargs)
        blogpages=self.get_children().live().order_by('-first_published_at')

        
        context['blogpages']=blogpages
        
        return context

    @route(r"^category/(?P<cat_name>[-\w]*)/$", name="category_view")
    def category_view(self, request, cat_name):
        context =self.get_context(request)
        try:
            category=BlogCategory.objects.get(name=cat_name)
            message="Showing Result for category: "+str(category)
            blogpages=BlogPage.objects.filter(categories__name=category)
            blogpages=blogpages.order_by('-first_published_at')

        except:
            category=None
            message="No such Category exist."
            blogpages=None

        context['message']=message
        context['blogpages']=blogpages
        return  render(request, "blog/blog_index_page.html", context)

    @route(r"^tag/(?P<tag_name>[-\w]*)/$", name="tag_view")
    def tag_view(self, request, tag_name):
        context =self.get_context(request)

        tags=Tag.objects.all().values_list('name', flat=True)
        tags=list(set(list(tags)))
            
        if tag_name in tags:
            message="Showing Result for tag: "+str(tag_name)
            blogpages=BlogPage.objects.filter(tags__name=tag_name)
            blogpages=blogpages.order_by('-first_published_at')
            
        else:
            message="No such tag exist."
            blogpages=None
        
        context['message']=message
        context['blogpages']=blogpages
        return  render(request, "blog/blog_index_page.html", context)
    
    @route(r"^archives/", name="archive_view")
    def archive_view(self, request):
        context =self.get_context(request)

        tags=Tag.objects.all().values_list('name', flat=True)
        tags=list(set(list(tags)))
    
        context['message']="Archives Page"
        context['tags']=tags
        return  render(request, "blog/archives.html", context)
    
   

class BlogPageTag(TaggedItemBase):
    content_object=ParentalKey(
        'BlogPage',
        related_name='taggeditems',
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
        index.SearchField('intro', partial_match=True),
        index.SearchField('body',partial_match=True),
        index.FilterField('categories'),
        index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ], heading="Blog Information"),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery Images")
    ]

    def get_context(self, request,*args, **kwargs):
        context=super().get_context(request,*args, **kwargs)
        blogpages=self.get_siblings()
        context['page']=self
        return context

    def prev_page(self):
        if self.get_prev_sibling():
            return self.get_prev_sibling().url
        else:
            return None
            # self.get_siblings().first().url
            
    def next_page(self):
        if self.get_next_sibling():
            return self.get_next_sibling().url
        else:
            return None 
            # self.get_siblings().last().url

    

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

