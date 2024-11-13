from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Machine, Partner

# Create your views here.

def home(request):
    page_title = 'Home Page'
    partners = Partner.objects.filter(active=True).order_by('order')

    context = {
        'page_title': page_title,
        'partners': partners

    }
    return render(request, 'website/home.html', context)

def about(request):
    page_title = 'About'
    
    context = {
        'page_title': page_title
    }

    return render(request, 'website/about.html', context)

def shop(request):
    page_title = 'Shop'
    machines = Machine.objects.all()
    paginator = Paginator(machines,5)

    page_number = request.GET.get('page')
    machines = paginator.get_page(page_number)

    context = {
        'page_title': page_title,
        'machines': machines
    }

    return render(request, 'website/shop.html', context)

def machine_detail(request,slug):
    page_title = 'Machine Details'
    machine = get_object_or_404(Machine,slug=slug)
    referer = request.META.get('HTTP_REFERER','shop/')
    images = machine.images.all();

    context = {
        'page_title': page_title,
        'machine': machine,
        'referer': referer,
        'images': images
    }

    return render (request,'website/machine-detail.html',context)