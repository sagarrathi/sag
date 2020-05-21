from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from wagtail.core.models import Page
from wagtail.search.models import Query

from blog.models import BlogPage

from django.db.models import Q

def search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        # search_results = Page.objects.live().search(search_query)
        search_results = BlogPage.objects.filter(Q(body__contains=search_query)|Q(title__contains=search_query))
        query = Query.get(search_query)
        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    message="Got "+str(len(search_results))+" results for search term: " +str(search_query)
    return TemplateResponse(request, 'search/search.html', {
        'message': message,
        'blogpages': search_results,
    })

