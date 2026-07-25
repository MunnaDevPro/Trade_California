from django.db import models
from solo.models import SingletonModel
from tinymce.models import HTMLField

class SiteSettings(SingletonModel):
    site_name = models.CharField(max_length=255, default="Trade California International")
    tagline = models.CharField(max_length=255, default="Connecting American Products with International Markets")
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    
    # Contact Info
    contact_email = models.EmailField(blank=True, default="contact@tradecalifornia.com")
    contact_phone = models.CharField(max_length=50, blank=True, default="+1 (800) 123-4567")
    
    # Social Media Links
    facebook_url = models.URLField(blank=True, default="https://facebook.com")
    twitter_url = models.URLField(blank=True, default="https://twitter.com")
    linkedin_url = models.URLField(blank=True, default="https://linkedin.com")
    
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

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# --- Page Settings Models ---

class HomePageSettings(SingletonModel):
    hero_headline = models.CharField(max_length=255, default="Expand Your Global Reach")
    hero_subtext = models.TextField(default="Premium Trade & International Business Platform")
    hero_background = models.ImageField(upload_to='site/hero/', blank=True, null=True)
    hero_opacity_percentage = models.PositiveIntegerField(default=30, help_text="Opacity of the hero background image (0-100)")
    hero_cta_text = models.CharField(max_length=50, default="Register Now", blank=True)
    hero_cta_link = models.CharField(max_length=255, default="/registration/", blank=True)
    
    def __str__(self):
        return "Home Page Settings"
    
    class Meta:
        verbose_name = "Home Page Settings"
        verbose_name_plural = "Home Page Settings"

class AboutPageSettings(SingletonModel):
    hero_headline = models.CharField(max_length=255, default="About Us")
    hero_subtext = models.TextField(default="Trade California International")
    hero_background = models.ImageField(upload_to='site/hero/', blank=True, null=True)
    hero_opacity_percentage = models.PositiveIntegerField(default=20, help_text="Opacity of the hero background image (0-100)")
    
    mission_statement = models.TextField(blank=True, default="To connect American businesses with global opportunities.")
    vision_statement = models.TextField(blank=True, default="Empowering trade without borders.")
    
    cta_headline = models.CharField(max_length=255, default="Ready to Partner With Us?")
    cta_subtext = models.TextField(default="Join thousands of verified businesses expanding their global footprint through Trade California International.", blank=True)
    cta_button_text = models.CharField(max_length=50, default="Apply to Partner Program")
    cta_button_link = models.CharField(max_length=255, default="/registration/")

    def __str__(self):
        return "About Page Settings"
    
    class Meta:
        verbose_name = "About Page Settings"
        verbose_name_plural = "About Page Settings"

class ProductsPageSettings(SingletonModel):
    hero_headline = models.CharField(max_length=255, default="Our Products")
    hero_subtext = models.TextField(default="Explore our premium catalog of American products.")
    hero_background = models.ImageField(upload_to='site/hero/', blank=True, null=True)
    hero_opacity_percentage = models.PositiveIntegerField(default=20, help_text="Opacity of the hero background image (0-100)")

    def __str__(self):
        return "Products Page Settings"
    
    class Meta:
        verbose_name = "Products Page Settings"
        verbose_name_plural = "Products Page Settings"

class ServicesPageSettings(SingletonModel):
    hero_headline = models.CharField(max_length=255, default="Our Services")
    hero_subtext = models.TextField(default="Comprehensive solutions for international trade.")
    hero_background = models.ImageField(upload_to='site/hero/', blank=True, null=True)
    hero_opacity_percentage = models.PositiveIntegerField(default=20, help_text="Opacity of the hero background image (0-100)")

    def __str__(self):
        return "Services Page Settings"
    
    class Meta:
        verbose_name = "Services Page Settings"
        verbose_name_plural = "Services Page Settings"

class ContactPageSettings(SingletonModel):
    hero_headline = models.CharField(max_length=255, default="Contact Us")
    hero_subtext = models.TextField(default="Get in touch with our expert team today.")
    hero_background = models.ImageField(upload_to='site/hero/', blank=True, null=True)
    hero_opacity_percentage = models.PositiveIntegerField(default=20, help_text="Opacity of the hero background image (0-100)")

    def __str__(self):
        return "Contact Page Settings"
    
    class Meta:
        verbose_name = "Contact Page Settings"
        verbose_name_plural = "Contact Page Settings"

class RegistrationPageSettings(SingletonModel):
    hero_headline = models.CharField(max_length=255, default="Partner Registration")
    hero_subtext = models.TextField(default="Join our global network of verified trade partners.")
    hero_background = models.ImageField(upload_to='site/hero/', blank=True, null=True)
    hero_opacity_percentage = models.PositiveIntegerField(default=20, help_text="Opacity of the hero background image (0-100)")

    def __str__(self):
        return "Registration Page Settings"
    
    class Meta:
        verbose_name = "Registration Page Settings"
        verbose_name_plural = "Registration Page Settings"
