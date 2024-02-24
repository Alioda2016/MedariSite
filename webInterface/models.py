from django.db import models

# Create your models here.

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/')
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
    date_added = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title




