from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
import resend

from .models import Banner, SocialLink, Stat, NavigationItem
from .models import About, Skill, Interest, Education, Project
from .forms import ContactForm


def index(request):

    # Fetch portfolio data
    banner = Banner.objects.first()
    socials = SocialLink.objects.all()
    stats = Stat.objects.all()
    nav_items = NavigationItem.objects.all()
    about = About.objects.first()
    skills = Skill.objects.all()
    interests = Interest.objects.all()
    education_list = Education.objects.all().order_by('-period')
    projects = Project.objects.all()

    # Contact form
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            # Save message to database
            contact = form.save()

            # Send email using Resend API
            try:
                resend.api_key = settings.RESEND_API_KEY

                resend.Emails.send({
                    "from": "Portfolio <onboarding@resend.dev>",
                    "to": [settings.CONTACT_EMAIL],
                    "subject": f"New Portfolio Message from {contact.name}",
                    "reply_to": [contact.email],
                    "text": f"""
You received a new message from your portfolio.

Name: {contact.name}
Email: {contact.email}

Message:
{contact.message}
"""
                })

                messages.success(
                    request,
                    "Message sent successfully!"
                )

            except Exception as e:
                print("RESEND EMAIL ERROR:", e)

                messages.error(
                    request,
                    "Your message was received, but email notification could not be sent."
                )

            # Redirect after POST
            return redirect('index')

    else:
        form = ContactForm()

    # Render portfolio page
    return render(
        request,
        'app/index.html',
        {
            'banner': banner,
            'socials': socials,
            'stats': stats,
            'nav_items': nav_items,
            'about': about,
            'skills': skills,
            'interests': interests,
            'education_list': education_list,
            'projects': projects,
            'form': form,
        }
    )




# from django.shortcuts import render, redirect
# from django.conf import settings
# from django.contrib import messages
# from django.core.mail import EmailMessage

# from .models import Banner, SocialLink, Stat, NavigationItem
# from .models import About, Skill, Interest, Education, Project
# from .forms import ContactForm


# def index(request):

#     # Fetch portfolio data
#     banner = Banner.objects.first()
#     socials = SocialLink.objects.all()
#     stats = Stat.objects.all()
#     nav_items = NavigationItem.objects.all()
#     about = About.objects.first()
#     skills = Skill.objects.all()
#     interests = Interest.objects.all()
#     education_list = Education.objects.all().order_by('-period')
#     projects = Project.objects.all()

#     # Contact form
#     if request.method == 'POST':

#         form = ContactForm(request.POST)

#         if form.is_valid():

#             # Save message to database
#             contact = form.save()

#             # Send email
#             email = EmailMessage(
#                 subject=f"New Portfolio Message from {contact.name}",

#                 body=f"""
# You received a new message from your portfolio.

# Name: {contact.name}
# Email: {contact.email}

# Message:
# {contact.message}
# """,

#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 to=[settings.CONTACT_EMAIL],

#                 # User's email will be used when you click Reply
#                 reply_to=[contact.email],
#             )

#             # Try to send email
#             try:
#                 email.send(fail_silently=False)

#                 messages.success(
#                     request,
#                     "Message sent successfully!"
#                 )

#             except Exception as e:
#                 print("EMAIL ERROR:", e)

#                 messages.error(
#                     request,
#                     "Your message was received, but email notification could not be sent."
#                 )

#             # Redirect after POST
#             return redirect('index')

#     else:
#         form = ContactForm()

#     # Render portfolio page
#     return render(
#         request,
#         'app/index.html',
#         {
#             'banner': banner,
#             'socials': socials,
#             'stats': stats,
#             'nav_items': nav_items,
#             'about': about,
#             'skills': skills,
#             'interests': interests,
#             'education_list': education_list,
#             'projects': projects,
#             'form': form,
#         }
#     )