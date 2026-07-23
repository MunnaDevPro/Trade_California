from django.db import models
from solo.models import SingletonModel
from tinymce.models import HTMLField

class SiteSettings(SingletonModel):
    site_name = models.CharField(max_length=255, default="Trade California International")
    tagline = models.CharField(max_length=255, default="Connecting American Products with International Markets")
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    
    # Hero Section
    hero_headline = models.CharField(max_length=255, default="Expand Your Global Reach")
    hero_subtext = models.TextField(default="Premium Trade & International Business Platform")
    hero_background = models.ImageField(upload_to='site/', blank=True, null=True)
    hero_cta_text = models.CharField(max_length=50, default="Register Now")
    hero_cta_link = models.CharField(max_length=255, default="/registration/")
    
    # About Section
    about_text = HTMLField(blank=True, default="<p>Trade California International is your trusted partner...</p>")
    mission_statement = models.TextField(blank=True, default="To connect American businesses with global opportunities.")
    vision_statement = models.TextField(blank=True, default="Empowering trade without borders.")
    
    # Contact Info
    contact_email = models.EmailField(blank=True, default="contact@tradecalifornia.com")
    contact_phone = models.CharField(max_length=50, blank=True, default="+1 (800) 123-4567")
    
    # External integrations
    chatbot_embed_code = models.TextField(blank=True, help_text="Paste your Tawk.to or other chatbot script here")
    analytics_script = models.TextField(blank=True, help_text="Google Analytics or similar")

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"

class CompanyValue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Heroicons icon name, e.g. 'GlobeAltIcon'", blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='mentors/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class NavigationLink(models.Model):
    label = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label

class FooterLink(models.Model):
    label = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label
