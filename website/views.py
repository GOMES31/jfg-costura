from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm

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
    images = machine.images.all()

    context = {
        'machine': machine,
        'images': images
    }

    print(images)

    if request.headers.get('HX-Request'):
        return render(request, 'website/partials/machine-detail.html', context )
    else:
        return redirect('shop')

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():

            # Retrieve form data
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            # Send the email
            subject = f"jfgcostura.com - Email de {name}"
            message_body = f"Nome: {name}\nEmail: {email}\n\nMensagem: \n{message}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]

            try:
                send_mail(subject, message_body, from_email, recipient_list)
                messages.success(request, "Email enviado com sucesso!")

                return render(request, 'website/partials/email-sent.html', {"name": name})
            except Exception as e:
                messages.error(request, f"Um erro ocorreu a tentar enviar o email!")

        return render(request, 'website/partials/contact.html', {"form": form, "errors": form.errors})

    else:
        form = ContactForm()
    
    return render(request, 'website/partials/contact.html', {"form": form})