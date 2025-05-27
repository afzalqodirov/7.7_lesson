from django.db import models
from django.utils.text import slugify

class Star(models.Model):
    name = models.CharField(max_length=100)
    distance_from_earth = models.PositiveIntegerField()
    image = models.ImageField(upload_to='stars', default='stars/default.jpg')
    slug = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
