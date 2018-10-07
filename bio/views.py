from django.shortcuts import render
from bio.models import Gene
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home(request):
    return render(request, 'bio/home.html')


def search(request):
    q = request.GET.get('q')
    results = None
    # page_range = None
    if q:
        results = Gene.objects.filter(
            Q(keywords__name__contains=q) | Q(name__icontains=q) | Q(code__icontains=q)).distinct()
        paginator = Paginator(results, 25)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            results = paginator.get_page(page)

        except (EmptyPage, PageNotAnInteger):
            results = paginator.get_page(0)

        # # Get the index of the current page
        # index = results.number - 1  # edited to something easier without index
        # # This value is maximum index of your pages, so the last page - 1
        # max_index = len(results.paginator.page_range)
        # # You want a range of 7, so lets calculate where to slice the list
        # start_index = index - 3 if index >= 3 else 0
        # end_index = index + 3 if index <= max_index - 3 else max_index
        # # Get our new page range. In the latest versions of Django page_range returns
        # # an iterator. Thus pass it to list, to make our slice possible again.
        # page_range = list(results.paginator.page_range)[start_index:end_index]
        #

    return render(request, 'bio/search.html', {'q': q, 'results': results, 'page_range': ""})


def contact(request):
    return render(request, 'bio/contact.html')

def about(request):
    return render(request, 'bio/about.html')