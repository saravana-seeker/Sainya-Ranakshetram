from django.shortcuts import render
from django.http import HttpResponse
from .search_query import esearch_result

# Create your views here.


def search_result(request):
    results = []
    search_term = ""
    if request.GET.get('search'):
        search_term = request.GET['search']
    else:
        print("please specify something")
    results = esearch_result(search_term)
    print(results)
    context = {'results': results, 'count': len(
        results), 'search_term': search_term}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'About.html')
