from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Machine, Partner

# Create your views here.

def home(request):
    partners = Partner.objects.filter(active=True).order_by('order')
    if request.headers.get('HX-Request'):
        return render(request, 'website/partials/home.html', {'partners': partners })
    
    return render(request, 'website/index.html', {'partners': partners })

def about(request):
    if request.headers.get('HX-Request'):
        return render(request, 'website/partials/about.html')
    else:
        return redirect('home')

def shop(request):
    machines = Machine.objects.all().order_by('name') 
    paginator = Paginator(machines,5)

    page_number = request.GET.get('page')
    machines = paginator.get_page(page_number)


    if request.headers.get('HX-Request'):
        return render(request, 'website/partials/shop.html', {'machines': machines})
    else:
        return redirect('home')

def machine_detail(request,slug):
    machine = get_object_or_404(Machine,slug=slug)
    referer = request.META.get('HTTP_REFERER','shop/')
    images = machine.images.all()

    context = {
        'machine': machine,
        'referer': referer,
        'images': images
    }

    if request.headers.get('HX-Request'):
        return render(request, 'website/partials/machine-detail.html', context )
    else:
        return redirect('shop')

def contact(request):
    
    return render(request, 'website/partials/contact.html')