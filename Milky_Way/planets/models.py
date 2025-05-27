from django.db import models
from django.utils.text import slugify

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=100)
    distance_from_earth = models.PositiveIntegerField()
    slug = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

