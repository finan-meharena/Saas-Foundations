from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit


def home_page_view(request, *args, **kwargs ):
    PageVisit.objects.create()
    queryset = PageVisit.objects.all()
    
    context = {
        "title" : "Hello finan",
        "page_visit_count": queryset.count() 
    }
    
    return render(request, 'home.html', context=context)

def about_view(request):
    context = {
        "title" : "About page",
    }
    return render(request, 'about.html',context )
