from django.shortcuts import render, redirect
from .models import News
from .forms import AdmissionForm
from django_ratelimit.decorators import ratelimit
from django.http import JsonResponse

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
    return render(request, 'main/admission_presentations.html')

def programs(request):
    return render(request, 'main/programs.html')

def contact(request):
    return render(request, 'main/contact.html')

def news_list(request):
    news = News.objects.all().order_by('-published_at')
    return render(request, 'main/news_list.html', {'news': news})

@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def register(request):
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
