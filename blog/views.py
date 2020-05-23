from blog.models import BlogPage, Tag, BlogCategory
from django.template.response import TemplateResponse
from django.shortcuts import render


def archives(request):    
    tags=Tag.objects.all().values_list('name', flat=True)
    tags=list(set(list(tags)))
    
    cats=BlogCategory.objects.all().values_list('name', flat=True)
    tags=list(set(list(cats)))
    
    cat_dict={}
    for c in cats:
        cat_dict[c]=BlogPage.objects.filter(categories__name=c)

    tag_dict={}
    for t in tags:
        tag_dict=BlogPage.objects.filter(tags__name=t)

    context={}    
    context['tag_dict']=tag_dict
    context['cat_dict']=cat_dict
    
    
    return render(request, 'blog/archives.html', context=context)


