from django.contrib import admin

from blog.models import *
# Register your models here.

admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Service)
admin.site.register(Subscribe)
admin.site.register(PortfolioCategory)
admin.site.register(Order)



@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['full_name','phone_number','title']



class ContactEmailInline(admin.StackedInline):
    model = EmailContact
    max_num = 10
    extra = 1


class ContactNumberInline(admin.StackedInline):
    model = PhoneContact
    max_num = 10
    extra = 1

MAX_OBJECTS = 1

@admin.register(ContactSettings)
class AdminGeneralSettings(admin.ModelAdmin):
    inlines = [ContactEmailInline,ContactNumberInline]


    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)



class SectionAboutInline(admin.StackedInline):
    model = SectionAbout
    max_num = 20
    extra = 1

@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    inlines = [SectionAboutInline]

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)



class PortfolioImagesInline(admin.StackedInline):
    model = PortfolioImages
    max_num = 100
    extra = 1


@admin.register(Portfolio)
class AdminPortfolioCategory(admin.ModelAdmin):
    inlines = [PortfolioImagesInline]
    # list_display = ['name','project_count']


