from django.shortcuts import render
from django.shortcuts import render, redirect


# Create your views here.

from .models import Banner, SocialLink, Stat, NavigationItem
from .models import About
from .models import Skill
from .models import Interest
from .models import Education
from .models import Project
from .forms import ContactForm

def index(request):
    banner = Banner.objects.first()
    socials = SocialLink.objects.all()
    stats = Stat.objects.all()
    nav_items = NavigationItem.objects.all()
    about = About.objects.first()
    skills = Skill.objects.all()
    interests = Interest.objects.all()
    education_list = Education.objects.all().order_by('-period')
    projects = Project.objects.all()

    success = False  # success message flag

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()  # reset form
        # else: errors automatically available in form
    else:
        form = ContactForm()
    
    return render(request, 'app/index.html', {
        'banner': banner,
        'socials': socials,
        "stats": stats,
        'nav_items': nav_items,
        'about': about,
        'skills': skills,
        'interests': interests,
        'education_list': education_list,
        'projects': projects,
        'form': form,
        'success': success,

    })


# from .models import CV

# def home(request):
#     cv = CV.objects.last()   # latest CV
#     return render(request, "index.html", {"cv": cv})



