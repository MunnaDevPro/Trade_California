from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Product(models.Model):
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(400, 400)],
                                     format='JPEG',
                                     options={'quality': 85})
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Product #{self.id}"

