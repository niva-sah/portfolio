from django.db import models

# Create your models here.


class Banner(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    description = models.TextField()
    profile_image = models.ImageField(upload_to="profile/")
    resume_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name



  

class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
    ]

    platform = models.CharField(
        max_length=50,
        choices=PLATFORM_CHOICES,
        default='facebook'
    )
    url = models.URLField()
    icon = models.ImageField(upload_to='social_icons/', null=True, blank=True)

    def __str__(self):
        return f"{self.platform} - {self.url}"

    



class Stat(models.Model):
    number = models.CharField(max_length=20)  # e.g. "10+"
    label = models.CharField(max_length=50)   # e.g. "Projects Completed"

    def __str__(self):
        return self.label
    

class NavigationItem(models.Model):
    label = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.label




class About(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="about/")   # media/about/ folder ma save huney
    intro = models.TextField()
    experience = models.TextField()
    goal = models.TextField()

    def __str__(self):
        return self.name



class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True, null=True)  # optional for grouping
    color_class = models.CharField(max_length=50, blank=True, null=True)  # optional for custom highlight

    def __str__(self):
        return self.name


from django.db import models

class Interest(models.Model):
    image = models.ImageField(upload_to='interests/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description[:20] if self.description else "Interest"





from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=200)      # e.g., Bachelor in Computer Engineering
    institution = models.CharField(max_length=200) # e.g., Nepal Engineering College
    university_or_board = models.CharField(max_length=200, blank=True, null=True)  # e.g., Pokhara University
    period = models.CharField(max_length=50)       # e.g., 2022 – Present
    description = models.TextField(blank=True, null=True)  # optional additional info

    def __str__(self):
        return f"{self.degree} - {self.institution}"


from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)       # e.g., College Info Chatbot
    description = models.TextField()               # project details
    link = models.URLField(blank=True, null=True)  # optional project link
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # optional project image

    def __str__(self):
        return self.title




class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # automatically set timestamp

    def __str__(self):
        return f"{self.name} - {self.email}"
    



# class CV(models.Model):
#     file = models.FileField(upload_to='cv/')
    
#     def __str__(self):
#         return "User CV"

