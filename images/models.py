from django.db import models

# Create your models here.
class ImageUrl(models.Model):
    original_url=models.CharField(max_length=500)
    compressed_url=models.CharField(max_length=500)

    def __str__(self):
        return self.original_url
