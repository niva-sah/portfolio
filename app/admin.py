from django.contrib import admin

# Register your models here.


from .models import Banner, SocialLink, Stat, NavigationItem

admin.site.register(Banner)
admin.site.register(SocialLink)
admin.site.register(Stat)
admin.site.register(NavigationItem)



from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("name","goal")


   
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'color_class')



from .models import Interest

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ( 'image', 'description')



from .models import Education

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'university_or_board', 'period')




from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')


from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')



# from .models import CV

# admin.site.register(CV)

