from django.shortcuts import render
from blog.models import BlogCategory
from blog.models import Tag

def tags_cats(request):
    tags=Tag.objects.all().values_list('name', flat=True)
    tags=list(set(list(tags)))
    
    cats=BlogCategory.objects.all().values_list('name', flat=True)
    context={}
    context['tags']=tags
    context['cats']=cats

    return context