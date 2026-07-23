from django.db import models

class OfficeLocation(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. Head Office, Orange County Office")
    address = models.TextField()
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    map_embed_url = models.URLField(max_length=500, blank=True, help_text="Google Maps embed src URL")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('closed', 'Closed'),
    ]

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    admin_notes = models.TextField(blank=True, help_text="Internal notes for admins")

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"
