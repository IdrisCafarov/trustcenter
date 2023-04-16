from django.db import models
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings




# Create your models here.

#####################  Contact About Part ###########################

class ContactSettings(models.Model):
    adress = models.CharField(max_length=200)

    def __str__(self):
        return 'Contact About'


    class Meta:
        verbose_name = "Contact About"
        verbose_name_plural = "Contact About"



class PhoneContact(models.Model):
    number = models.CharField(max_length=20)
    general = models.ForeignKey(ContactSettings, on_delete=models.CASCADE, related_name="number")


class EmailContact(models.Model):
    email = models.EmailField()
    general = models.ForeignKey(ContactSettings,on_delete=models.CASCADE, related_name="email")


###################################################################

############### About Part ###########################

class About(models.Model):

    def __str__(self):
        return 'About Settings'

    class Meta:
        verbose_name = "About Settings"
        verbose_name_plural = "About Settings"

    pass


class SectionAbout(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="section")
    image = models.FileField(upload_to="section_images",null=True)
    text = models.TextField()



####################################



class Service(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()
    image = models.FileField(upload_to="service_images",null=True)


    def __str__(self):
        return self.name

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=150)
    project_count = models.IntegerField(default=0,editable=False)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Portfolio Category"
        verbose_name_plural = "Portfolio Categories"


class Portfolio(models.Model):
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name="portfolio", null=True)
    name = models.CharField(max_length=150)
    main_image = models.FileField(upload_to="portfolio_images",null=True)
    video = models.CharField(max_length=2000,null=True)
    service = models.ManyToManyField(Service,related_name="portfolio")
    text = models.TextField(null=True)
    date = models.DateField(auto_now_add=True,null=True)
    live_demo_link = models.CharField(max_length=2000,null=True)
    """soon"""
    def __str__(self):
        return self.name


class PortfolioImages(models.Model):
    image = models.FileField(upload_to="portfolio_images",null=True)
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE, related_name="image")




class Author(models.Model):
    name = models.CharField(max_length=150)
    image = models.FileField(upload_to="author_pp",null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name



class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="blog",null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="blog",null=True)
    main_image = models.FileField(upload_to="blog_image",null=True)
    title = models.CharField(max_length=150,null=True)
    text = RichTextField(null=True)
    tag = models.ManyToManyField(Tag, related_name="blog")
    date = models.DateField(auto_now_add=True)
    click = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return self.title

    def get_num_clicks(self):
        return self.clicks

    @classmethod
    def get_most_clicked(cls):
        return cls.objects.all().order_by('-click').first()



class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.full_name







class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email



class Order(models.Model):
    currentStage = models.CharField(max_length=3000)
    chooseWebSite = models.CharField(max_length=3000)
    professionalNeed = models.CharField(max_length=3000)
    duration = models.CharField(max_length=3000)
    #########
    name = models.CharField(max_length=3000)
    surname = models.CharField(max_length=3000)
    email = models.EmailField()
    phone = models.CharField(max_length=3000)


    ####################
    description = models.TextField()
    projectDeatils = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


@receiver(post_save, sender=Order)
def delete_free_time(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Order yarandi',
            f'Current Stage: {instance.currentStage}\nChoose WebSite: {instance.chooseWebSite}\nprofessional Need: {instance.professionalNeed}\nDuration : {instance.duration}/nCustomer Informations\nCustomer: {instance.name} {instance.surname}\nEmail: {instance.email}\nPhone: {instance.phone}\n\n\nAbout Project\n\nDescription: {instance.description}\nProject Deatils : {instance.projectDeatils}',
            settings.EMAIL_HOST_USER,
            ['ravan.xankisiyev.032@gmail.com'],
            fail_silently=True,
        )

