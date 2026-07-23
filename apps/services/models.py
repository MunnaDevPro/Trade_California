from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

class ServiceType(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Upload an icon or SVG")
    short_description = models.TextField(help_text="For the homepage cards")
    detailed_description = HTMLField(blank=True, help_text="For the services detail page")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
