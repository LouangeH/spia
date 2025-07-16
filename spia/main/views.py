from django.shortcuts import render, redirect, get_object_or_404
from main.models import News
from main.forms import AdmissionForm, RegisterForm, NewsForm
from django_ratelimit.decorators import ratelimit
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    #news = News.objects.all().order_by('-published_at')[:3]  # Dernières 3 actualités
    return render(request, 'main/home.html')
def about(request):
    return render(request, 'main/about.html')

def courses(request):
    return render(request, 'main/courses.html')

def governance(request):
    return render(request, 'main/governance.html')

def admission(request):
    return render(request, 'main/admission_presentation.html')

def programs(request):
    return render(request, 'main/programs.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"Message from {name} via Contact Page"
        full_message = f"From: {name} <{email}>\n\n{message}"
    
        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['info@spia.bi'],
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully.")
        return redirect('contact')  # or render with a success message
    return render(request, 'main/contact.html')

def news_list(request):
    news = News.objects.all().order_by('-published_at')
    return render(request, 'main/news_list.html', {'news': news})

# News CRUD
@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form})

@login_required
def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/news_form.html', {'form': form})

@login_required
def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect('admin_dashboard')



#@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def register_student(request):
    if request.method == "POST":
        print(request.POST)
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            print("Formulaire valide !")
            form.save()
            return redirect('home')
        else:
            print("Erreurs du formulaire :", form.errors)
    else:
        form = AdmissionForm()
    return render(request, 'main/admission.html', {'form': form})

def boarding(request):
    return render(request, 'main/boarding.html')

def campus(request):
    return render(request, 'main/school_life.html')

# tenders/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tender
from .forms import TenderForm
from datetime import date

# Afficher tous les appels d’offres
def tender_list(request):
    tenders = Tender.objects.filter(deadline__gte=date.today()).order_by('-published_at')
    return render(request, 'tenders/tender_list.html', {'tenders': tenders})

# Créer un appel d’offre
@login_required
def tender_create(request):
    if request.method == 'POST':
        form = TenderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tender_list')
    else:
        form = TenderForm()
    return render(request, 'tenders/tender_form.html', {'form': form})

# Modifier un appel d’offre
@login_required
def tender_edit(request, pk):
    tender = get_object_or_404(Tender, pk=pk)
    form = TenderForm(request.POST or None, request.FILES or None, instance=tender)
    if form.is_valid():
        form.save()
        return redirect('tender_list')
    return render(request, 'tenders/tender_form.html', {'form': form})

# Supprimer un appel d’offre
@login_required
def tender_delete(request, pk):
    tender = get_object_or_404(Tender, pk=pk)
    if request.method == 'POST':
        tender.delete()
        return redirect('tender_list')
    return render(request, 'tenders/tender_confirm_delete.html', {'tender': tender})

@login_required
def admin_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('admin_dashboard')
    else:
        form = RegisterForm()
    return render(request, 'admin/register.html', {'form': form})


def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('admin_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'admin/login.html', {'form': form})

@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required
def admin_dashboard(request):
    news_list = News.objects.all().order_by('-published_at')
    return render(request, 'admin/dashboard.html', {'news_list': news_list})